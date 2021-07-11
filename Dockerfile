FROM python:3.8-slim
##Install libraries
RUN apt-get -y update && apt-get install -y libpq-dev python3-dev g++

RUN mkdir /home/app
WORKDIR /home/app
COPY . .
RUN pip3 install -r requirements.txt
WORKDIR /home/app
ENV PYTHONPATH=/home/app
CMD ["gunicorn"  , "-w","2", "--threads", "2","-b", "0.0.0.0:8000", "application:application"]
