#!/usr/bin/python3
# -*- coding=utf8 -*-

import uuid
import json
import time
from rediscon import RedisPool 

conn = RedisPool().conn 
def delay(msg):
    """
    delay a task for 5s
    """
    msg["id"] = str(uuid.uuid4())
    value = json.dumps(msg)
    retry_ts = time.time() + 5
    conn.zadd("delay-queue", {value:retry_ts})


def loop():
    while True:
        # get one message
        values = conn.zrangebyscore("delay-queue", 0, time.time(), start=0, num=1)
        if not values:
            time.sleep(1)
            continue
        value = values[0]
        success = conn.zrem("delay-queue", value)
        if success:
            msg = json.loads(value)
            print(msg)

delay({"id": None})
loop()
