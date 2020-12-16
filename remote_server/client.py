#!/usr/bin/python3
# -*- coding=utf8 -*-


import socket

host = ""
port = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    data = "a"
    while data != b'end':
        s.sendall(bytes(input(), encoding="utf-8"))
        data = s.recv(1024)
        print(data)
