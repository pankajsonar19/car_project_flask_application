FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN mkdir /db
WORKDIR /db
ENTRYPOINT [ "sqlite3" ]