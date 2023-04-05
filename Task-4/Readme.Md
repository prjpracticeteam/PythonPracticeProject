Links:
------
https://medium.com/aeturnuminc/configure-prometheus-and-grafana-in-dockers-ff2a2b51aa1d
https://docs.docker.com/config/daemon/prometheus/
https://medium.com/geekculture/how-to-monitor-docker-metrics-using-prometheus-grafana-707b970f1f06
https://www.linkedin.com/pulse/docker-monitoring-cadvisor-prometheus-grafana-abhishek-rana?trk=pulse-article_more-articles_related-content-card
https://www.metricfire.com/blog/monitoring-docker-containers-with-cadvisor/#How-to-use-cAdvisor-for-container-monitoring
https://cloudsbaba.com/how-to-use-prometheus-to-monitoring-java-application/


Step-1: Prometheus
----------------
--> I have copied the dockerfile and the war file from Task-2
--> I am installing the prometheus on docker container
--> I have created a prometheus.yml with some scrapes and content. Ip here used is the private Ip of the instance as the docker containers will be patched with the ports on the localhost.
--> To configure docker metrics, i have created a file in /etc/docker/daemon.json and pasted this content
{
  "metrics-addr" : "0.0.0.0:9323"
}
Metrics can be found at "localhost:9323/metrics"
--> To further know the docker metrics, i have installed a cadvisor docker container by following one of the above links with a docker command "sudo docker run --volume=/:/rootfs:ro --volume=/var/run:/var/run:ro --volume=/sys:/sys:ro --volume=/var/lib/docker/:/var/lib/docker:ro --volume=/dev/disk/:/dev/disk:ro -p 8080:8080 -d--name=cadvisor gcr.io/cadvisor/cadvisor:latest".
Metrics can be found at "localhost:8080/metrics"
--> later i have added the metric scrape to the prometheus.yml file.
--> To configure node metrics, i have installed the node exporter from a tar file to /usr/local/bin/
Metrics can be found at "localhost:9100/metrics"
--> Later to monitor the jvm metrics of the tomcat app that i have to deploy on a container, i have followed one of the above links and chatgpt.
--> I have downloaded jvm exporter from the github and kept it in tomcat_exporters folder and then created a config.yaml file with content 
lowercaseOutputName: true
lowercaseOutputLabelNames: true
rules:
  - pattern: 'java.lang<type=(.*)><>(.*)'
    name: jmx_$1_$2
    type: GAUGE

--> I have used the command "docker run -d -p 82:80 -p 8088:8088 -p 8082:8080 --name tomcat_metrics -e CATALINA_OPTS="-javaagent:/opt/jmx_prometheus_javaagent-0.18.0.jar=8088:/opt/prometheus-jmx-config.yaml" sample1:latest" to start the tomcat app and collected the metrics.
Metrics can be found at "localhost:8088"
--> I have given scraped for cadvisor, docker, tomcat and node_exporter in prometheus.yml file.
--> After this i have deployed the prometheus container and checked the targets for all.
the docker command: "docker run -d --name prometheus -p 9090:9090 -v ./prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus --config.file=/etc/prometheus/prometheus.yml"


Grafana:
--------
--> To install the grafana in a container, i have followed one of the links above and used the docker command:
"docker run -d --name grafana -p 3000:3000 grafana/grafana"
--> set the datasource to prometheus with the link: "http://<private-ip>:9100"
--> I have setup the following dashboards:
1. Docker and Host Monitoring w/ Prometheus
2. Docker Monitoring
3. JVM Dashboard
4. Node Exporter Full
Find the ID's of these dashboards from the internet.