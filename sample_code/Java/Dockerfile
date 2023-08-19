FROM eclipse-temurin:17-jdk-jammy as build

COPY src/SampleClient.java /src/
RUN javac /src/SampleClient.java && ls -al /src

FROM eclipse-temurin:17-jdk-jammy

COPY --from=build src/*.class /app/

ENTRYPOINT cd app && java SampleClient

