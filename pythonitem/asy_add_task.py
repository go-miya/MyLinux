import asyncio
from redisfunc.rediscon import RedisPool
import time

async def add_event(n):
    print('starting ' + str(n))
    await asyncio.sleep(1)
    print('ending ' + str(n))
    return n

async def main(loop):

    # added_tasks = []
    while True:
        # await asyncio.sleep(2)
        print("waiting for input")
        n = conn.lpop("queue")
        while n is None:
            await asyncio.sleep(0.5)
            n = conn.lpop("queue")
        print('adding ' + str(n))
        loop.create_task(add_event(n))
        # task = loop.create_task(add_event(n))
        # added_tasks.append(task)
        await asyncio.sleep(0)

conn = RedisPool().conn

loop = asyncio.get_event_loop()
results = loop.run_until_complete(main(loop))
print(results)
