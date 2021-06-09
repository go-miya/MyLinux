from redis import Redis
from rediscluster import RedisCluster
# import enviroment
import logging

logging.basicConfig(level=logging.DEBUG)

startup_nodes = [
    {"host": "127.0.0.1", "port": "7000"},
    {"host": "127.0.0.1", "port": "7001"},
    {"host": "127.0.0.1", "port": "7002"},
    {"host": "127.0.0.1", "port": "7003"},
    {"host": "127.0.0.1", "port": "7004"},
    {"host": "127.0.0.1", "port": "7005"},
]

# redis_client = Redis(host=enviroment.CONFIG['redis_host'], port=enviroment.CONFIG['redis_port'])

redis_cluster_client = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

def test():
    redis_cluster_client.set("foo", "hh")
    return redis_cluster_client.get("foo")
test()