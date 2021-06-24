FROM ubuntu
ENV PYTHONPATH=/mysite:

WORKDIR /mysite
COPY ../.. .

RUN apt-get update && apt install -y python3-pip && \
pip3 install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple tornado==6.1 && \
pip3 install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple grpcio==1.37.0 grpcio-tools==1.37.0 && \
pip3 install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple jaeger-client==4.3.0 opentracing==2.4.0
