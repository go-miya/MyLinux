FROM ubuntu:16.04
ENV GOPATH=/mycodis/gopath
WORKDIR /mycodis

RUN apt-get update
RUN apt-get -y install wget
RUN apt-get -y install git
RUN apt-get -y install gcc automake autoconf libtool make

# install go
RUN wget https://golang.org/dl/go1.7.3.linux-amd64.tar.gz -O go.tar.gz
RUN rm -rf /usr/local/go && tar -C /usr/local -xzf go.tar.gz
RUN export PATH=$PATH:/usr/local/go/bin
RUN export PATH=$PATH:$GOPATH/bin

# install codis
RUN mkdir -p $GOPATH/src/github.com/CodisLabs
RUN cd $GOPATH/src/github.com/CodisLabs && git clone https://github.com/CodisLabs/codis.git -b release3.2
RUN cd $GOPATH/src/github.com/CodisLabs/codis

RUN export PATH=$PATH:/usr/local/go/bin && export PATH=$PATH:$GOPATH/bin && cd $GOPATH/src/github.com/CodisLabs/codis && make

RUN cd $GOPATH/src/github.com/CodisLabs/codis && \
./admin/codis-dashboard-admin.sh start && \
./admin/codis-proxy-admin.sh start && \
./admin/codis-server-admin.sh start && \
./admin/codis-fe-admin.sh start
