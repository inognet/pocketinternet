from jinja2 import Environment, PackageLoader

def generate_ipv4_addr(pod_n, host, backbone=False):
    octets = []
    if backbone:
        octets.append("172")
    else:
        octets.append("10")

    octets.append(pod_n)

    octets.append(str(host))

    return ".".join(octets)

def generate_ipv6_addr(pod_n, host, backbone=False):
    address = "fd00:"

    left, right = pod_n.split(".")
    if backbone:
        address += "bb::{}:{}:{}"
    else:
        address += "{}:{}::{}"

    return address.format(left, right, host)

j2env = Environment(
    loader=PackageLoader('pocketnet', 'templates')
)