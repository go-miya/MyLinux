#!/usr/bin/python3
# -*- coding=utf8 -*-

import tornado
import tornadis


#def ping_callback(result):
#    print(result)
#
#@tornado.gen.coroutine
#def main():
#    client.async_call("PING", callback=ping_callback)
#    yield tornado.gen.sleep(1)


@tornado.gen.coroutine
def talk_to_redis():
    result = yield client.call("PING")
    print(result)


client = tornadis.Client(host="localhost", port=6379, autoconnect=True)

loop = tornado.ioloop.IOLoop.instance()
loop.run_sync(talk_to_redis)

