FROM tomcat:8.5



EXPOSE 8080

ADD target/sparkjava-hello-world-1.0.war
Entrypoint ["/sparkjava-hello-world-1.0.war"]
