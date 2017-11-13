import os

import docker

from pocketnet import CONFIG_ROOT
from pocketnet.util import generate_ipv4_addr, generate_ipv6_addr, j2env
from pocketnet.pods import get_pod_network_name
from pocketnet.routing.util import generate_as_number, compile_peering_details


def create_bird_config(pod_n, router_n, config):
    print("[PocketInternet][Pod {}] Configuring bird_{}".format(
        pod_n,
        router_n))
    template = j2env.get_template('bird.conf.j2')
    as_number = generate_as_number(pod_n)

    environment = {
        "our_as": as_number,
        "peerings": compile_peering_details(pod_n, router_n, "ipv4", config)
    }

    filename = "bird_{}.conf".format(router_n)
    config = template.render(**environment)

    config_dir = os.path.join(CONFIG_ROOT, "pod_{}".format(pod_n))
    with open(os.path.join(config_dir, filename), 'w') as fp:
        print("[PocketInternet][Pod {}] Writing Config File: {}{}{}".format(
            pod_n,
            config_dir,
            os.sep,
            filename))
        fp.write(config)


def create_bird6_config(pod_n, router_n, config):
    print("[PocketInternet][Pod {}] Configuring bird6_{}".format(
        pod_n,
        router_n))
    template = j2env.get_template('bird6.conf.j2')
    as_number = generate_as_number(pod_n)

    environment = {
        "our_as": as_number,
        "peerings": compile_peering_details(pod_n, router_n, "ipv6", config)
    }

    filename = "bird6_{}.conf".format(router_n)
    config = template.render(**environment)

    config_dir = os.path.join(CONFIG_ROOT, "pod_{}".format(pod_n))
    with open(os.path.join(config_dir, filename), 'w') as fp:
        print("[PocketInternet][Pod {}] Writing Config File: {}{}{}".format(
            pod_n,
            config_dir,
            os.sep,
            filename))
        fp.write(config)


def deploy_birds(pod_n, router_n, config):
    print("[PocketInternet][Pod {}] Generating Bird Configs".format(pod_n))
    create_bird_config(pod_n, router_n, config)
    create_bird6_config(pod_n, router_n, config)

    devel_flags = config['config'].get('devel_flags', [])

    # Now we have our configs created, let's deploy some containers
    docker_client = docker.from_env()

    config_dir = os.path.join(CONFIG_ROOT, "pod_{}".format(pod_n))
    config_vol = {"bind": "/opt/pocketinternet", "mode": "ro"}

    # deploy bird first
    bird_image = config['config']['images']['bird']
    bird_container = docker_client.containers.create(
        bird_image,
        detach=True,
        name="pod{}_bird4_{}".format(pod_n, router_n),
        volumes={
            os.path.join(config_dir, "bird_{}.conf".format(router_n)): {
                "bind": "/etc/bird/bird.conf",
                "mode": "rw"
            },
            CONFIG_ROOT: config_vol
        }
    )

    # Now bird6
    bird_6_container = docker_client.containers.create(
        bird_image,
        detach=True,
        name="pod{}_bird6_{}".format(pod_n, router_n),
        command="/usr/sbin/bird6 -d",
        volumes={
            os.path.join(config_dir, "bird6_{}.conf".format(router_n)): {
                "bind": "/etc/bird/bird6.conf",
                "mode": "rw"
            },
            config_dir: config_vol
        }
    )

    # Hook the newly created containers up to networks
    if "no_networks" not in devel_flags:
        # grab the networks first
        bb_network_name = "backbone"
        internal_network_name = get_pod_network_name(pod_n)

        bb_network = docker_client.networks.list(names=[bb_network_name])[0]
        internal_network = docker_client.networks.list(names=[internal_network_name])[0]

        router_host_ip = router_n + 10

        # Connect bird4 then bird6
        bb_network.connect(
            bird_container,
            ipv4_address=generate_ipv4_addr(
                pod_n,
                router_host_ip,
                backbone=True
            )
        )
        internal_network.connect(
            bird_container,
            ipv4_address=generate_ipv4_addr(
                pod_n,
                router_host_ip
            )
        )

        bb_network.connect(
            bird_6_container,
            ipv6_address=generate_ipv6_addr(
                pod_n,
                router_host_ip,
                backbone=True
            )
        )
        internal_network.connect(
            bird_6_container,
            ipv6_address=generate_ipv6_addr(
                pod_n,
                router_host_ip
            )
        )

    bird_container.start()
    bird_6_container.start()
