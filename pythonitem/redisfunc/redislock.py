#!/usr/bin/python3
# -*- coding=utf8 -*-

import random
from redisfunc.rediscon import RedisPool


def redis_lock(func):
    def wrapper(*args, **kwargs):
        tag = random.randint(1, 1000)  # define a random num
        conn = RedisPool().conn
        while True:
            if conn.set("conn.lock", str(tag), nx=True, ex=5):
                print("lock successfully")
                func(*args, **kwargs)
                if conn.get("conn.lock") == str(tag):
                    conn.delete("conn.lock")
                break
    return wrapper


class RedisLock:
    def __init__(self, key, expired_time=None):
        self.key = key
        self.expired_time = expired_time
        self.client = RedisPool().conn

    def __enter__(self):
        if not self.client.set(self.key, 1, ex=self.expired_time):
            # 并发操作下直接抛出异常
            # raise_biz_exc(ExcCode.OP_CONCURRENT_EXCEPTION, u'操作过于频繁')
            raise Exception("hhh")

    def __exit__(self, exc_type, exc_value, tb):
        self.client.delete(self.key)
        print("hhhh")


if __name__ == "__main__":
    with RedisLock("xing:zhao"):
        print(1 / 0)

