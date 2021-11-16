# FROM haproxy:1.7
# RUN apt-get update && apt-get install -y  rsyslog
# RUN service rsyslog start
# COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg

FROM haproxy:2.3
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
COPY blacklist_agent.lst /usr/local/etc/haproxy/blacklist_agent.lst
COPY whitelist_agent.lst /usr/local/etc/haproxy/whitelist_agent.lst