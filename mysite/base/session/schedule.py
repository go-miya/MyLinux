from .base_session import BaseScheduleSession
from ..redisfunc.rediscon import RedisPool
import typing
import uuid
import asyncio
import json


class ScheduleSession(BaseScheduleSession):

    def __init__(self):
        self.conn = RedisPool().conn
        super(ScheduleSession, self).__init__()

    def _add_to_task_queue(self, task: str, module_name: str):
        task_queue_name = module_name + ":queue"
        self.conn.lpush(task_queue_name, task)

    async def service_call(self, module_name: str, pkg: typing.Dict):
        pkg["module_name"] = module_name
        pkg["key"] = str(uuid.uuid4())
        self._add_to_task_queue()
        res = self.conn.lpop(pkg["key"])
        while not res:
            await asyncio.sleep(1)
            res = self.conn.lpop(pkg["key"])
        return json.loads(res)
