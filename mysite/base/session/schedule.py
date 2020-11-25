from .base_session import BaseScheduleSession
from ..redisfunc.rediscon import RedisPool
import typing
import asyncio
import json
import time
from tornado import gen


class ScheduleSession(BaseScheduleSession):

    def __init__(self):
        self.conn = RedisPool().conn
        super(ScheduleSession, self).__init__()

    async def result_call(self, pkg: typing.Dict, module_name: str):
        task_queue_name = module_name + ":queue"
        self.conn.lpush(task_queue_name, json.dumps(pkg))
        res = self.conn.lpop(pkg["key"])
        while not res:
            await asyncio.sleep(0.1)
            res = self.conn.lpop(pkg["key"])
        return res

    async def service_call(self, module_name: str, pkg: typing.Dict, timeout: int=1):
        try:
            res = await gen.with_timeout(time.time()+timeout, self.result_call(pkg, module_name))
            return json.loads(res)
        except TimeoutError as e:
            print(e)
        return {}
