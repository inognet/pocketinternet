FROM ubuntu:17.10
MAINTAINER Pocket Internet Team

RUN apt-get update
RUN apt-get install --no-install-recommends -y \
                    curl traceroute mtr-tiny net-tools \
                    telnet iputils-tracepath netcat nmap \
                    iperf3 iproute2 dnsutils tcpdump iputils-ping
