FROM ubuntu:latest

RUN apt update && \
    apt install curl -y && \
    apt install unzip -y && \
    curl -O -L "https://github.com/grafana/loki/releases/download/v2.8.0/promtail-linux-amd64.zip" && \
    unzip "promtail-linux-amd64.zip" && \
    chmod a+x "promtail-linux-amd64" && \
    mv promtail-linux-amd64 /usr/local/bin/promtail && \
    mkdir -p /etc/promtail

COPY promtail-config.yaml /etc/promtail/config.yaml

CMD ["promtail", "-config.file=/etc/promtail/config.yaml"]



#FROM grafana/promtail:2.8.0

#WORKDIR promtail

#RUN mkdir -p /etc/promtail

#COPY promtail-config.yaml /etc/promtail/config.yaml

#EXPOSE 9080 0 

#CMD ["promtail", "-config.file=/etc/promtail/config.yaml"]



