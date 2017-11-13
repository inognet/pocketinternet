import json
import os


def configure_docker():
    if os.getuid() != 0:
        print("[PocketInternet] To configure docker this command must be run as root. Please re-run the command either with sudo or as root.")
    else:
        print("[PocketInternet] Configuring Docker")
        docker_config = {
            "bip": "192.168.200.1/24",
            "fixed-cidr": "192.168.200.0/24",
            "ipv6": True,
            "fixed-cidr-v6": "fc00::/8"
        }
        with open(os.path.join(os.sep, 'etc', 'docker', 'daemon.json'), 'w') as fp:
            json.dump(docker_config, fp)

        print("[PocketInternet] Restarting Docker")
        os.system('systemctl restart docker')
        print("[PocketInternet] Restarted Docker")
