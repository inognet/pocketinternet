FROM pocketinternet/base:0.5
LABEL Description="Pocket Internet BIRD image" Version="0.2" Maintainer="Pocket Internet Team"

RUN apt-get update
RUN apt-get install -y bird && mkdir /run/bird

# Create volume for configuration files
VOLUME /etc/bird/

# Adds custom environments to Bird daemon
ADD envvars /etc/bird/

# Exposes BGP port by default.
EXPOSE 179/tcp

# Starts bird service
CMD /usr/sbin/bird -d
