FROM ubuntu:latest

# Java Installation
RUN apt-get update && apt-get install -y openjdk-19-jdk

# Apache Installation
RUN apt-get install -y apache2 && apt-get install -y wget

# Tomcat9 Installation
RUN wget https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.55/bin/apache-tomcat-9.0.55.tar.gz && \
    tar xzf apache-tomcat-9.0.55.tar.gz && \
    rm apache-tomcat-9.0.55.tar.gz && \
    mv apache-tomcat-9.0.55 /usr/local/tomcat9

# Copy war file to tomcat webapps directory
COPY SampleWebApp.war /usr/local/tomcat9/webapps/

# Expose port 8080 for Tomcat
EXPOSE 8080 8088

# Configure Apache2 as a reverse proxy for Tomcat
RUN a2enmod proxy && \
    a2enmod proxy_http && \
    echo "ProxyPass / http://localhost:8080/SampleWebApp/" >> /etc/apache2/sites-available/000-default.conf


ADD tomcat_exporter_jars/jmx_prometheus_javaagent-0.18.0.jar /opt/jmx_prometheus_javaagent-0.18.0.jar
ADD prometheus-jmx-config.yaml /opt/prometheus-jmx-config.yaml


# Start Apache and Tomcat on container startup
CMD service apache2 start && /usr/local/tomcat9/bin/catalina.sh run 

# use this command to get the jvm metrics
##docker run -d -p 82:80 -p 8088:8088 -p 8082:8080 --name tomcat_metrics -e CATALINA_OPTS="-javaagent:/opt/jmx_prometheus_javaagent-0.18.0.jar=8088:/opt/prometheus-jmx-config.yaml" sample1:latest





