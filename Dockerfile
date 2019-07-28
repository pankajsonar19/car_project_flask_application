# car_project Flask application Dockerfile

# using the ubuntu:latest image from docker-hub
FROM ubuntu:latest

# basic update all command
RUN apt-get update -y

# installing the python, pip and some necessary python package dependencies
RUN apt-get install -y python-pip python-dev build-essential

# add the whole current project content to car-project directory on docker image
ADD . /car-project

# make it as current working directory to run further commands
WORKDIR /car-project

# copy the requirements.txt to docker so that everytume we run this requirements will be already available
COPY requirements.txt .

# install the requirements
RUN pip install -r requirements.txt

# optional: to expose port on which the docker should run the app
EXPOSE 5000

# set/export the env variable for the flask application which states the main entry point for flask app
ENV FLASK_APP = main.py

# entry point to run flask app. generally python for any flask applications
ENTRYPOINT ["python"]

# command include what needs to be followed after python. here python main.py will run our project
CMD ["main.py"]