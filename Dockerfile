# get Ubuntu base image
FROM	ubuntu:18.04 AS base
MAINTAINER Jim Schwoebel <jim.schwoebel@gmail.com>

# set working directory
WORKDIR /usr/src/app
COPY . /usr/src/app

# set environment variables 
ENV DEBIAN_FRONTEND=noninteractive 

# now run sudo apt update commands
RUN apt-get update \
  && apt-get install -y python3-pip python3 \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && apt-get install -y apt-utils \
  && apt-get install -y autoconf \
  && apt-get install -y automake \
  && apt-get install -y build-essential \
  && apt-get install -y cmake \
  && apt-get install -y ffmpeg \
  && apt-get install -y gcc \
  && apt-get install -y g++ \
  && apt-get install -y git \
  && apt-get install -y libasound-dev \
  && apt-get install -y libffi-dev \
  && apt-get install -y libldap2-dev \
  && apt-get install -y libpq-dev \
  && apt-get install -y libpulse-dev \
  && apt-get install -y libsasl2-dev \
  && apt-get install -y libsm6 \ 
  && apt-get install -y libsndfile1 \
  && apt-get install -y libtool \
  && apt-get install -y libxml2-dev \
  && apt-get install -y libxslt1-dev \ 
  && apt-get install -y libxext6 \
  && apt-get install -y make \ 
  && apt-get install -y m4 \
  && apt-get install -y opus-tools \
  && apt-get install -y portaudio19-dev \
  && apt-get install -y sox \
  && apt-get install -y swig \
  && apt-get install -y tesseract-ocr \
  && apt-get install -y tree \
  && apt-get install -y tzdata \
  && apt-get install -y unzip \
  && apt-get install -y wget \
  && apt-get install libgl1-mesa-glx \
  && apt-get install imagemagick
  
RUN	pip3 install -r requirements.txt

# set working directory
WORKDIR	/usr/src/app
