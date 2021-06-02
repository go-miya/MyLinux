# Mysite

This file mysite contains all code about http service and downstream service.

Both the http service and downstream service run in docker

We need execute the Dockerfile in
 <a href="docker/dockerbase">dockerbase</a> by:

`docker build -t mysite_base:v1 .`

And then execute the Dockerfile respectively in 
<a href="docker/dockerhttp">docker/dockerhttp/a> and
<a href="docker/dockerdownstream">docker/dockerdownstream</a>
by:

`docker build -t mysite_http:v1 .`

`docker build -t mysite_downstream:v1 .`