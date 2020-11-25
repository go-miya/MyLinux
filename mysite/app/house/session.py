from base.session.base_session import BaseProcessSession
import json
import asyncio


class HouseSession(BaseProcessSession):
    def __init__(self):
        self.queue = "house:queue"
        super(HouseSession, self).__init__()

    async def asy_call_task(self):
        task_list = {
            "helloworld": self.process_helloworld
        }
        while True:
            pkg = self.redis_conn.lpop(self.queue)
            while not pkg:
                await asyncio.sleep(0.5)
                pkg = self.redis_conn.lpop(self.queue)
            pkg = json.loads(pkg)
            self.loop.create_task(task_list.get(pkg["action"])(pkg))
            await asyncio.sleep(0)

    async def process_helloworld(self, pkg: dict):
        await asyncio.sleep(1)
        res = {"result": "helloworld"}
        key = pkg.get("key")
        self.write_to_middle_part(key, res)

