# Pocket Internet Container Images

Pocket Internet services run as Docker containers. This is the repository of Dockerfiles necessary to build the container images. The images themselves can be found on docker hub.


### Base image

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

### Client image

This image is the base container with the OpenSSH daemon installed and running (login details `root/pocket`). Its purpose is to be used as a client machine in the Pocket Internet to perform connectivity and application testing.

### BIRD image

This image is the current BGP router and the main container on which the Pocket Internet is run. As BIRD daemons are IPv4 or IPv6 only, a container will have to be run for each protocol.

### HTTP Static image

This container runs a default install nginx to serve static content over http.

### Reference commands

- To download an image or specific version, run `docker pull pocketinternet/base:0.X`. If you don't specify the version tag, the command will assume `latest`.
- To build a new version
    + Clone the repository (`git clone https://github.com/inognet/pocketinternet.git`).
    + In the `containers/base` folder run `docker build -t pocketinternet/base:0.X .` with a valid version number (replace `0.X`).
    + Once the container is built, test it in an interactive way with `docker run -it pocketinternet/base-container:0.X`.
    + Then push it to the docker hub registry: `docker push pocketinternet/base-container:0.X`
