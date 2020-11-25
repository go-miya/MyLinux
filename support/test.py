import tornado.ioloop
import tornado.web
from tornado import gen
import asyncio
import time


async def func():
    await asyncio.sleep(5)
    return "aa"


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        try:
            res = await gen.with_timeout(time.time() + 6, func())
            print(res)
            self.write("Hello, world" + res)
        except TimeoutError as e:
            print("timeout")

def callback():
    print("timeout")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()



# import tornado.web
# from tornado.ioloop import IOLoop
# from tornado import gen
#
# from tornado.concurrent import run_on_executor
# from concurrent.futures import ThreadPoolExecutor   # `pip install futures` for python2
#
# MAX_WORKERS = 16
#
# class TestHandler(tornado.web.RequestHandler):
#     executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)
#
#     """
#     In below function goes your time consuming task
#     """
#
#     @run_on_executor
#     def background_task(self):
#         sm = 0
#         for i in range(10 ** 8):
#             sm = sm + 1
#
#         return sm
#
#     @tornado.gen.coroutine
#     def get(self):
#         """ Request that asynchronously calls background task. """
#         res = yield self.background_task()
#         print("bbb")
#         self.write(str(res))
#
# class TestHandler2(tornado.web.RequestHandler):
#     @gen.coroutine
#     def get(self):
#         self.write('Response from server')
#         print("aaa")
#         self.finish()
#
#
# application = tornado.web.Application([
#     (r"/A", TestHandler),
#     (r"/B", TestHandler2),
#     ])
#
# application.listen(5000)
# IOLoop.instance().start()
