
import gevent
from gevent.queue import JoinableQueue

import random


# def do_work(item):
#     print(f"task {item} 正在被执行")
#     gevent.sleep(random.randint(1,3))
#     print(f"task {item} 已结束")
#
#
# def worker():
#     while True:
#         work, item = q.get()
#         try:
#             work(item)
#         finally:
#             q.task_done()
#
#
# q = JoinableQueue()
# for i in range(20):
#     gevent.spawn(worker)
#
#
# while True:
#     for item in range(1, 10):
#         q.put((do_work, item))
#     q.join()  # block until all tasks are done

class Parent:
    def start(self):
        raise NotImplementedError

class Child(Parent):
    def __init__(self):
        super(Child, self).start()
    def start(self):
        print("Child start")

c = Child()
c.start()
