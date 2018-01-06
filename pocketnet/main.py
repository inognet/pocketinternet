#!/usr/bin/env python
import argparse
import os
import yaml
import sys

from pocketnet import CONFIG_ROOT
from pocketnet.backbone import create_backbone_network
from pocketnet.dockerconfig import configure_docker
from pocketnet.pods import create_pod_internal_network
from pocketnet.pods.base import setup_base_container
from pocketnet.pods.dns import setup_dns_container
from pocketnet.pods.web import setup_web_container
from pocketnet.routing.bird import deploy_birds


def run():
    """
        Entrypoint for Pocket Internet
    """
    parser = argparse.ArgumentParser(description="PocketInternet - Lab Tool")
    parser.add_argument('-c', '--config',
            dest='config_file',
            default="lab.yml",
            help='YAML Configuration File')

    subparsers = parser.add_subparsers(help="Sub Commands", dest="subparser")
    subparsers.add_parser('configure-docker', help="Perform one-off configuration of docker daemon.")

    subparsers.add_parser('setup', help="Set up PocketInternet Lab")
    subparsers.add_parser('teardown', help="Tear down PocketInternet Lab")

    args = parser.parse_args()

    if args.subparser == "configure-docker":
        configure_docker()
    elif args.subparser == "setup":
        # TODO Modularize and move out of run() function
        print("[PocketInternet] Starting Setup Process")

        print("[PocketInternet] Loading Lab Configuration")
        configuration = None

        try:
            with open(args.config_file) as cfp:     # cfp => config file pointer
                configuration = yaml.load(cfp)
            print("[PocketInternet] Lab Configuration Loaded")
            if "title" in configuration:
                print("[PocketInternet] Lab Title: {}".format(
                    configuration['title']
                ))
            print(
                "[PocketInternet] Lab Contains {} Pods and {} Peerings".format(
                    len(configuration['pods']),
                    len(configuration['peerings'])
                )
            )
        except IOError as ex:
            print("IOError: {}".format(ex))
            sys.exit(1)

        devel_flags = configuration['config'].get('devel_flags', [])

        if "no_networks" not in devel_flags:
            create_backbone_network()

        for pod in configuration['pods']:
            pod_number = str(pod['number'])
            print("[PocketInternet] Deploying Pod: {}".format(pod_number))

            assert "." in pod_number, "Pod Number Format Invalid. Pod Numbers must be in the format XX.YYY"
            pod_n_left, pod_n_right = pod_number.split(".")
            assert int(pod_n_left) >= 16 and int(pod_n_left) <= 31, "Pod Number must be between 16 and 31 (Left Side of Period)"
            assert int(pod_n_right) >= 1 and int(pod_n_right) <= 255, "Pod Number must be between 1 and 255 (Right Side of Period)"

            # Create config dir
            config_dir = os.path.join(CONFIG_ROOT, "pod_{}".format(pod_number))
            if not os.path.exists(config_dir):
                os.makedirs(config_dir)

            # Create Pod Network
            create_pod_internal_network(pod_number)

            pod_routing = pod.get('routing', {'daemon': 'bird', 'number': 1})
            pod_routing_type = pod_routing.get('daemon', 'bird')
            pod_number_routers = pod_routing.get('number', 1)
            for router_number in range(pod_number_routers):
                if pod_routing_type == "bird":
                    deploy_birds(pod_number, router_number + 1, configuration)

            pod_kind = pod['kind']
            supported_kinds = {
                "web": setup_web_container,
                "dns": setup_dns_container,
                "base": setup_base_container
            }

            if pod_kind in supported_kinds:
                supported_kinds[pod_kind](pod)
            else:
                print("[PocketInternet] Pod kind of '{}' was not recognised.".format(pod_kind))
    elif args.subparser == "teardown":
        # TODO
        pass

if __name__ == "__main__":
    main()
