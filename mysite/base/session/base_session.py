from abc import ABCMeta, abstractmethod
from base.redisfunc.rediscon import RedisPool
import asyncio
import json

class BaseScheduleSession(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def service_call(self, module_name, pkg):
        pass


class BaseProcessSession(metaclass=ABCMeta):
    def __init__(self):
        self.redis_conn = RedisPool().conn
        self.loop = asyncio.get_event_loop()


    @abstractmethod
    async def asy_call_task(self):
        pass

    def write_to_middle_part(self, key: str, res: dict):
        print("add res to queue")
        self.redis_conn.lpush(key, json.dumps(res))
        print("add res finished")

    def run(self):
        self.loop.run_until_complete(self.asy_call_task())
