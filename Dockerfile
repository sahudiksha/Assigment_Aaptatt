FROM tomcat:8-jre8 
WORKDIR /app
COPY --from=build /app/target/hello-java-*.jar /app/app.jar
EXPOSE 8080
ENTRYPOINT ["sh", "-c"]
CMD ["java -jar app.jar"]

