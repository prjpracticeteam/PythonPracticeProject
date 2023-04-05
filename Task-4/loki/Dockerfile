FROM alpine:latest

# Install dependencies
RUN apk --no-cache add curl

# Download and install Loki
RUN curl -L https://github.com/grafana/loki/releases/download/v2.8.0/loki-linux-amd64.zip \
    -o loki.zip && \
    unzip loki.zip && \
    mv loki-linux-amd64 loki && \ 
    mv loki /usr/local/bin/ && \
    rm -rf loki.zip

# Create the Loki configuration file
RUN mkdir /etc/loki
COPY loki-config.yaml /etc/loki/config.yaml

EXPOSE 3100

# Set the command to run when the container starts
CMD ["loki", "-config.file=/etc/loki/config.yaml"]

