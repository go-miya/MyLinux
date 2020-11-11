#!/usr/bin/python3
# -*- coding=utf8 -*-

import time
from basefunc import timeout 
from redisfunc import redislock

@redislock.redis_lock
@timeout.time_out(2)
def task1():
    print("task1 start")
    time.sleep(2)
    print("task1 finished")


if __name__ == "__main__":
    task1()

