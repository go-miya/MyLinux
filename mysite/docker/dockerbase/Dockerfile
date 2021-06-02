FROM ubuntu
ENV PYTHONPATH=/mysite:

WORKDIR /mysite
COPY .. .

RUN apt-get update
RUN apt install -y python3-pip
RUN pip3 install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple tornado==6.1
RUN pip3 install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple grpcio==1.37.0 grpcio-tools==1.37.0

