# Mysite

This file mysite contains all code about http service and downstream service.
Both the http service and downstream service run in docker

We need execute the Dockerfile in
 <a href="docker/dockerbase">docker/dockerbase</a> by:

`docker build -t mysite_base:v1 .`

And then execute the Dockerfile respectively in 
<a href="docker/dockerhttp">docker/dockerhttp</a> and
<a href="docker/dockerdownstream">docker/dockerdownstream</a>
by:

`docker build -t mysite_http:test .`

`docker build -t mysite_downstream:test .`

Lastly, we just need to run the command below in the directory
<a href="docker">docker</a> in terminal.

`WORKSPACE=your_dir/mysite docker-compose -f your_dir/docker-compose.yml up`

