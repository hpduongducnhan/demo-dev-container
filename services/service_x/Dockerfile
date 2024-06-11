FROM python:3.12.3-bullseye

# proxy if your server behind proxy
ENV http_proxy http://proxy.hcm.fpt.vn:80              
ENV https_proxy http://proxy.hcm.fpt.vn:80             
ENV no_proxy=localhost,127.0.0.1,::1,172.24.222.112

# make sure your container could access internet to get dev and debug tools
RUN apt update -y
RUN apt install -y --no-install-recommends \
    make gcc build-essential python-dev\
    libpq-dev \
    mime-support media-types \
    telnet iputils-ping curl htop vim procps net-tools \
    && rm -rf /var/lib/apt/lists/*

# setup working directory,
WORKDIR /workspace/service_x

RUN mkdir -p /workspace/service_x/core

# image already has pip3, if not work, change to pip or pip3.x (x is python version - pip3.12)
# install poetry 
RUN pip3 install --upgrade pip \
    && pip3 install poetry wheel 
