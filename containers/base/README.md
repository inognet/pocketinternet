# Base container image

The base image is used in all other containers in order to provide a uniform troubleshooting toolset across the board. These tools are:

- curl
- traceroute
- mtr
- net-tools
- telnet
- iputils-tracepath
- netcat
- nmap
- iperf3
- iproute2
- dnsutils
- tcpdump
- iputils-ping

This image does not do anything by itself, although it can be started as an interactive shell (`/bin/bash`) for troubleshooting.
