import atexit

import gevent
from gevent.queue import JoinableQueue


# class GeventPoolExecutor():
#     def __init__(self, max_works, ):
#         self._q = JoinableQueue(maxsize=max_works)
#         # self._q = Queue(maxsize=max_works)
#         for _ in range(max_works):
#             gevent.spawn(self.__worker)
#         atexit.register(self.__atexit)
#
#     def __worker(self):
#         while True:
#             fn,args,kwargs = self._q.get()
#             try:
#                 print(11)
#                 fn(*args,**kwargs)
#             except Exception as exc:
#                 print(f'函数 {fn.__name__} 中发生错误，错误原因是 {type(exc)} {exc} ')
#             finally:
#                 print(22)
#                 self._q.task_done()
#
#     def submit(self, fn,*args,**kwargs):
#         self._q.put((fn,args,kwargs))
#
#     def __atexit(self):
#         print('即将退出程序。')
#         self._q.join()

# g = GeventPoolExecutor(2)

import random
def do_work(item):
    print(f"task {item} 正在被执行")
    gevent.sleep(random.randint(1,3))
    print(f"task {item} 已结束")


def worker():
    while True:
        work, item = q.get()
        try:
            work(item)
        finally:
            q.task_done()


q = JoinableQueue()
for i in range(20):
    gevent.spawn(worker)


while True:
    for item in range(1, 10):
        q.put((do_work, item))
    q.join()  # block until all tasks are done

