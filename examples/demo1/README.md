# RIPE NCC Copenhagen Hackathon Demo

![IP addressing example](/docs/img/Sample_IP_addressing.png)

## VM Setup

Start from a clean Ubuntu 16.04 image with `docker` (17.10+) and `docker-compose` (1.7.1+) installed. Older versions may work but are untested.

We need to change the default `docker` network so the IP space does not overlap with Pocket Internet addressing:

```
vi /etc/docker/daemon.json
{
    "bip": "192.168.200.1/24",
    "fixed-cidr": "192.168.200.0/24",
    "ipv6": true,
    "fixed-cidr-v6": "fc00::/8"
}

service docker restart
```

You will need the following images for this lab:

```
root@ubuntu-xenial:/vagrant/examples/demo1# docker images

REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
pocketinternet/http-static   0.2                 6d63521aaa09        About an hour ago   227MB
pocketinternet/demo-dns      0.2                 f7b8d67825cc        About an hour ago   245MB
pocketinternet/client        0.2                 ab06a3b50ff2        About an hour ago   220MB
pocketinternet/bird          0.2                 9a21dc1b05c9        About an hour ago   216MB
```

## Starting the Lab


You are now ready to start the lab by running `docker-compose up`. This command will not exit and will stream container logging to the terminal!

```
root@ubuntu-xenial:/vagrant/examples/demo1# docker-compose up
Creating network "demo1_backbone_net" with driver "bridge"
Creating network "demo1_lan_net_17_1" with driver "bridge"
Creating network "demo1_lan_net_16_1" with driver "bridge"
Creating network "demo1_lan_net_16_2" with driver "bridge"
Creating demo1_bird16_2_1 ... 
Creating demo1_bird16_1_1 ... 
Creating demo1_bird16_2_1
Creating demo1_bird16_2_1 ... done
Creating demo1_client16_2_1 ... 
Creating demo1_nginx16_2_1 ... 
Creating demo1_client16_2_1
Creating demo1_bird16_1_1 ... done
Creating demo1_bird17_1_1 ... 
Creating demo1_bind16_1_1 ... 
Creating demo1_bird17_1_1
Creating demo1_bird17_1_1 ... done
Creating demo1_client17_1_1 ... 
Creating demo1_client17_1_1 ... done
```

In another window, you can confirm that the containers are running:

```
root@ubuntu-xenial:/vagrant/examples/demo1# docker ps
CONTAINER ID        IMAGE                            COMMAND                  CREATED             STATUS              PORTS               NAMES
f36a1111d8e4        pocketinternet/client:0.2        "bash -c 'ip route..."   5 minutes ago       Up 5 minutes        22/tcp              demo1_client17_1_1
4cff511c8f95        pocketinternet/demo-dns:0.2      "bash -c 'ip route..."   5 minutes ago       Up 5 minutes        53/tcp              demo1_bind16_1_1
f24cc5f1e532        pocketinternet/bird:0.2          "bash -c 'sysctl n..."   5 minutes ago       Up 5 minutes        179/tcp             demo1_bird17_1_1
b4a31bfd3768        pocketinternet/client:0.2        "bash -c 'ip route..."   5 minutes ago       Up 5 minutes        22/tcp              demo1_client16_2_1
a441f7feae41        pocketinternet/http-static:0.2   "bash -c 'ip route..."   5 minutes ago       Up 5 minutes        80/tcp              demo1_nginx16_2_1
3a9b6e2193ea        pocketinternet/bird:0.2          "bash -c 'sysctl n..."   5 minutes ago       Up 5 minutes        179/tcp             demo1_bird16_2_1
28d282be9cf3        pocketinternet/bird:0.2          "bash -c 'sysctl n..."   5 minutes ago       Up 5 minutes        179/tcp             demo1_bird16_1_1
```

You can SSH directly into the client container (10.17.1.101). To run commands in the other containers you can start a shell using `docker-compose exec <containername> /bin/bash`.


## Cleanup

To stop the lab, press `Ctrl+C` in the `docker-compose` window and, once it's done, run `docker-compose down` to remove all containers, networks etc.

```
Gracefully stopping... (press Ctrl+C again to force)
Stopping demo1_client17_1_1 ... done
Stopping demo1_bind16_1_1   ... done
Stopping demo1_bird17_1_1   ... done
Stopping demo1_client16_2_1 ... done
Stopping demo1_nginx16_2_1  ... done
Stopping demo1_bird16_2_1   ... done
Stopping demo1_bird16_1_1   ... done

root@ubuntu-xenial:/vagrant/examples/demo1# docker-compose down
Removing demo1_client17_1_1 ... done
Removing demo1_bind16_1_1   ... done
Removing demo1_bird17_1_1   ... done
Removing demo1_client16_2_1 ... done
Removing demo1_nginx16_2_1  ... done
Removing demo1_bird16_2_1   ... done
Removing demo1_bird16_1_1   ... done
Removing network demo1_backbone_net
Removing network demo1_lan_net_17_1
Removing network demo1_lan_net_16_1
Removing network demo1_lan_net_16_2
```
