FROM pocketinternet/base:0.4
MAINTAINER Pocket Internet Team

RUN apt-get update
RUN apt-get install -y bird && mkdir /run/bird

LABEL Description="Bird Internet routing daemon docker image" Version="0.1"

# Create volume for configuration files
VOLUME /etc/bird/

# Adds custom environments to Bird daemon
ADD envvars /etc/bird/

# Exposes BGP port by default. Expecify other protocol ports with 'docker run'
EXPOSE 179/tcp

# Starts bird service
#ENTRYPOINT service bird start
CMD /usr/sbin/bird -d
