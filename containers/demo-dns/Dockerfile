FROM pocketinternet/base:0.5
LABEL Description="Pocket Internet Demo-DNS image" Version="0.2" Maintainer="Pocket Internet Team"

RUN apt-get update
RUN apt-get install --no-install-recommends --no-install-suggests -y bind9

COPY files /etc/bind/

EXPOSE 53

CMD ["named", "-c", "/etc/bind/named.conf", "-g"]
