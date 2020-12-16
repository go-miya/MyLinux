#!/usr/bin/python3
# -*- coding=utf8 -*-

#import socket
#
#host = ""
#port = 9000
#
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.bind((host, port))
#    s.listen(1)
#    conn, addr = s.accept()
#    with conn:
#        print("Connected by", addr)
#        while True:
#            data = conn.recv(1024)
#            if not data:
#                break
#            conn.sendall(data)
#            print("receive: ", data)
#
import errno
import functools
import socket

import tornado.ioloop
from tornado
