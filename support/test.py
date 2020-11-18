import tornado.ioloop
import tornado.web
import asyncio


async def func():
    await asyncio.sleep(5)
    return "aa"


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        res = await func()
        self.write("Hello, world" + res)

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()