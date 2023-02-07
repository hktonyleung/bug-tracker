# pull official base image
FROM python:alpine

RUN apk --no-cache add curl

# set work directory
WORKDIR /usr/src/bug-tracker

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN python3 -m pip install --upgrade pip
COPY ./requirements.txt .
RUN python3 -m pip install -r requirements.txt

# copy project
COPY . .

