#!/usr/bin/python3
# -*- coding=utf8 -*-


from redisfunc.rediscon import RedisPool

conn = RedisPool().conn
while True:
    n = input()
    conn.lpush("queue", n)
