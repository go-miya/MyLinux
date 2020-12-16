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
from tornado.iostream import IOStream

async def handle_connection(connection, address):
    stream = IOStream(connection)
    message = await stream.read_until_close()
    print("message from client:", message.decode().strip())

def connection_ready(sock, fd, events):
    while True:
        try:
            connection, address = sock.accept()
        except BlockingIOError:
            return
        connection.setblocking(0)
        io_loop = tornado.ioloop.IOLoop.current()
        io_loop.spawn_callback(handle_connection, connection, address)

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(0)
    sock.bind(("", 8888))
    sock.listen(128)

    io_loop = tornado.ioloop.IOLoop.current()
    callback = functools.partial(connection_ready, sock)
    io_loop.add_handler(sock.fileno(), callback, io_loop.READ)
    io_loop.start()
