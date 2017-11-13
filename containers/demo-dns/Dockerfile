FROM pocketinternet/base-container:0.4
MAINTAINER Pocket Internet Team

RUN apt-get update
RUN apt-get install --no-install-recommends --no-install-suggests -y bind9

COPY files /etc/bind/


EXPOSE 53

CMD ["named", "-c", "/etc/bind/named.conf", "-g"]
