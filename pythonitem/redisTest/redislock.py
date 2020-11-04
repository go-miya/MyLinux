#!/usr/bin/python3
# -*- coding=utf8 -*-


import time
from rediscon import RedisPool

conn1 = RedisPool()#.conn
print(id(conn1))
#print(conn1.set('xing', 'hhh', nx=True, ex=2))
#time.sleep(2)
#print(conn1.get('xing'))
#
conn2 = RedisPool()#.conn
print(id(conn2))
#print(conn2.set('xing', 'hhh', nx=True, ex=2))
#time.sleep(2)
#print(conn2.get('xing'))
#
#class RedisLock:
#	def __init__(self):
#		self.conn = RedisPool().conn
#	
#	def usr
#
