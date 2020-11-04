#!/usr/bin/python3
# -*- coding=utf8 -*-

import redis


class RedisPool:
    redisPool = redis.ConnectionPool(host=host, port=port, decode_responses=True)
    pool = None
	
	def __new__(cls, *args, **kwargs):
		if not cls.instance_cache:
			cls.redisPool = redis.ConnectionPool(host='localhost', port=3306, decode_responses=True)
			cls.pool = super().__new__(cls)
		return cls.pool
	
	def __init__(self, host='localhost', port=6379):
		self.conn = redis.Redis(connection_pool=cls.redisPool)

