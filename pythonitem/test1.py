#!/usr/bin/python3
# -*- coding=utf8 -*-


import asyncio
import concurrent.futures

from rediscon import RedisPool

def func():
    conn = RedisPool().conn

    a = conn.blpop("queue")
