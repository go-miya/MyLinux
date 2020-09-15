import gevent
from gevent.queue import JoinableQueue
import random
import threading
import time

def do_work(item):
    print(f"task {item} 正在被执行")
    gevent.sleep(random.randint(1, 3))
    print(f"task {item} 已结束")


class WorkPool:
    def __init__(self, max_worker_num):
        self.max_worker_num = max_worker_num
        self.queue = JoinableQueue()
        self.set_worker()

    def set_worker(self):
        for i in range(self.max_worker_num):
            gevent.spawn(self.start_work)

    def start_work(self):
        while True:
            func, args = self.queue.get()
            try:
                func(*args)
            except Exception as e:
                print(f"func {func.__name__} error: {e}")
            finally:
                self.queue.task_done()

    def loop(self):
        while True:
            print(1)
            self.queue.join()

    def add_task(self, callback, *args):
        print(2)
        self.queue.put((callback, args))


def add_task_helper():
    for i in range(100):
        time.sleep(0.1)
        w.add_task(do_work, i)


w = WorkPool(5)
t1 = threading.Thread(target=add_task_helper())
t2 = threading.Thread(target=w.loop())
t1.start()
t2.start()
