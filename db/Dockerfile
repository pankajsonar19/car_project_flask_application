# Dockerfile for Sqlite database

# using ubuntu:latest image from docker-hub
FROM ubuntu:latest

# basic update all command
RUN apt-get update -y

# installing sqlite and its dependencies
RUN apt-get install -y sqlite3 libsqlite3-dev

# creating a directory to store the database
RUN mkdir /db

# using it as current working directory
WORKDIR /db

# entrypoint to our database which start with command sqlite3
ENTRYPOINT [ "sqlite3" ]