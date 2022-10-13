FROM tomcat:8.5

MAINTAINER Satheesh B "satheesh442@gmail.com"

EXPOSE 8080

USER root

COPY target/spark*.war webapps/my-app.war
