FROM ubuntu/bind9
WORKDIR /etc/bind/
COPY named.conf named.conf
COPY zones zones
RUN apt-get update \
    && apt-get install python3 dnsutils -y 
WORKDIR zones/
RUN python3 dns_script.py
WORKDIR /etc/bind/
