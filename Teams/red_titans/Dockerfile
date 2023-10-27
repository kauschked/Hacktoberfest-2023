FROM eclipse-temurin:17-jdk-jammy

WORKDIR /src

COPY src/Inception.java .
COPY src/inception.png .


#COPY --from=build src/*.class /app/

RUN javac /src/Inception.java
CMD ["java /src/Inception"]
#ENTRYPOINT ["javaXX", "InceptionXX"]
