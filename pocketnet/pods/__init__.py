import docker

from pocketnet.util import generate_ipv4_addr, generate_ipv6_addr


def get_pod_network_name(pod_n):
    return "pod_{}_internal".format(pod_n)


def create_pod_internal_network(pod_n):
    docker_client = docker.from_env()

    pod_network_name = get_pod_network_name(pod_n)
    pod_v4_network_address = generate_ipv4_addr(pod_n, 0)
    pod_v6_network_address = generate_ipv6_addr(pod_n, 0)

    pod_v4_subnet = "{}/24".format(pod_v4_network_address)
    pod_v6_subnet = "{}/48".format(pod_v6_network_address[:-1])

    print("[PocketInternet][Pod {}] Creating Pod Internal Network".format(
        pod_n))

    existing_networks = docker_client.networks.list(names=[pod_network_name])

    existing_networks = [net for net in existing_networks if net.name == pod_network_name]

    for network in existing_networks:
        print("[PocketInternet][Pod {}] Removing Existing Network: {}".format(
            pod_n,
            network.name))
        network.remove()

    v4_pool = docker.types.IPAMPool(
        subnet=pod_v4_subnet,
        gateway=generate_ipv4_addr(pod_n, 11)   # 10.XX.YYY.11 is router 1, default gw
    )
    v6_pool = docker.types.IPAMPool(
        subnet=pod_v6_subnet,
        gateway=generate_ipv6_addr(pod_n, 11)
    )

    ipam_config = docker.types.IPAMConfig(
        pool_configs=[v4_pool, v6_pool]
    )

    docker_client.networks.create(
        name=pod_network_name,
        enable_ipv6=True,
        ipam=ipam_config
    )

    print("[PocketInternet][Pod {}] Created Pod Internal Network".format(
        pod_n))
