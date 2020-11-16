import asyncio
from rediscon import RedisPool


async def add_event(n):
    print('starting ' + str(n))
    await asyncio.sleep(1)
    print('ending ' + str(n))
    return n


async def main(loop):

    added_tasks = []
    conn = RedisPool().conn
    while True:
        print("waiting for input")
        n = conn.blpop("queue")
        print('adding ' + str(n))
        task = loop.create_task(add_event(n))
        added_tasks.append(task)
        await asyncio.sleep(0)



loop = asyncio.get_event_loop()
results = loop.run_until_complete(main(loop))
print(results)
