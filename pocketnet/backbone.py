#!/usr/bin/env python
import sys

import docker


def create_backbone_network(name="backbone", v4_subnet="172.16.0.0/12", v6_subnet="fd00:bb::/48"):
    docker_client = docker.from_env()

    # Does the backbone network already exist?
    print("[BB] Checking for existing Backbone network")
    existing_backbone = docker_client.networks.list(names=[name])

    existing_backbone = [bb for bb in existing_backbone if bb.name == name]

    if existing_backbone:
        print("[BB] Backbone network already exists.")
    else:
        print("[BB] Backbone does not exist, Creating Backbone")
        v4_pool = docker.types.IPAMPool(subnet=v4_subnet)
        v6_pool = docker.types.IPAMPool(subnet=v6_subnet)

        ipam_config = docker.types.IPAMConfig(
            pool_configs=[v4_pool, v6_pool]
        )
        try:
            docker_client.networks.create(
                name=name,
                enable_ipv6=True,
                ipam=ipam_config
            )

            print("[BB] Created Backbone")
        except docker.errors.APIError as apierror:
            print("\r\n[BB] -!-!- UNABLE TO CREATE BACKBONE -!-!-")
            print("[BB] Docker Encountered an Error: {}".format(apierror))
            print("[BB] You will need to run pocketinternet on a machine which has no Docker containers or networks outside of the defaults.")
            print("[BB] At this point, you should then run 'sudo ./pocketinternet configure-docker' before re-running setup")
            print("[BB] -!-!- UNABLE TO CREATE BACKBONE -!-!-")

            sys.exit(1)
