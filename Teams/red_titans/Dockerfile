FROM eclipse-temurin:17-jdk-jammy as build

COPY src/Inception.java /src/
COPY src/inception.png /src/
RUN javac /src/Inception.java && ls -al /src

FROM eclipse-temurin:17-jdk-jammy

COPY --from=build src/*.class /app/

ENTRYPOINT cd app && java Inception


