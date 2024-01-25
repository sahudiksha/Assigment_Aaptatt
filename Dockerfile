FROM tomcat:8.5.83-jre17
COPY  ./target/sparkjava-hello-world-1.0.war   /usr/local/tomcat/webapps/
EXPOSE 8080
CMD ['bin/startaup.sh']
