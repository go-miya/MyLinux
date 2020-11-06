#!/usr/bin/python3
# -*- coding=utf8 -*-

import redis

class RedisPoolBase:
	redisPool = None
	def __new__(cls, *args, **kwrgs):
		if not cls.redisPool:
			cls.redisPool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
		return cls.redisPool


class RedisPool:
	
	def __init__(self):
		self.redisPool = RedisPoolBase() 
		self.conn = redis.Redis(connection_pool=self.redisPool)


