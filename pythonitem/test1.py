#!/usr/bin/python3
# -*- coding=utf8 -*-


import asyncio
import concurrent.futures
import time


def add_event_syn(n):
    print(f"ThreadPoolExecutor starting {n}")
    time.sleep(1)
    print(f"ThreadPoolExecutor ending {n}")




async def main():
    loop = asyncio.get_running_loop()
    while True:
        n = input()
        with concurrent.futures.ProcessPoolExecutor() as pool:
            result = await loop.run_in_executor(
                pool, add_event_syn, n)
            print('custom thread pool', result)


asyncio.run(main())
