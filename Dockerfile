FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ADD . /car-project
WORKDIR /car-project
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP = main.py
ENTRYPOINT ["python"]
CMD ["main.py"]