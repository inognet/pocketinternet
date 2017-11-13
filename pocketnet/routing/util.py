from pocketnet.util import generate_ipv4_addr, generate_ipv6_addr


def generate_as_number(pod_n):
    left_octet, right_octet = pod_n.split(".")
    as_number = "42000{0}{1:03d}".format(left_octet, int(right_octet))
    return as_number


def get_peer_detail_tuple(pod_n, router_n, peering):
    dest = None
    if (pod_n == peering['left_pod'] or pod_n == peering['right_pod']):
        if pod_n == peering['left_pod'] and router_n == peering['left_router']:
            dest = peering['right_pod'], peering['right_router']
        elif pod_n == peering['right_pod'] and router_n == peering['right_router']:
            dest = peering['left_pod'], peering['left_router']
    return dest


def compile_peering_details(pod_n, router_n, stack, config):
    parsed_peerings = []
    for peering in config['peerings']:
        dest = get_peer_detail_tuple(pod_n, router_n, peering)
        if dest:
            remote_as = generate_as_number(dest[0])
            if stack == "ipv4":
                remote_ip = generate_ipv4_addr(dest[0], dest[1] + 10, backbone=True)
            elif stack == "ipv6":
                remote_ip = generate_ipv6_addr(dest[0], dest[1] + 10, backbone=True)
            print(
                "[PocketInternet][Pod {}]\tPeering: Remote IP: {}\t\tRemote AS: {}".format(
                    pod_n,
                    remote_ip,
                    remote_as
                )
            )
            parsed_peerings.append({
                "remote_as": remote_as,
                "remote_ip": remote_ip
            })
    return parsed_peerings
