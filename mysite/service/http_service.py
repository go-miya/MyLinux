from tornado.web import Application
import tornado.ioloop
import tornado.httpserver
from .house import house
from .helloworld import helloworld_grpc
# from base import base


class App(Application):
    def __init__(self):
        handlers = [
            (r'/xing/helloworld', house.HelloWorld),
            (r'/xing/helloworld1', helloworld_grpc.HelloWorldHandler),
        ]
        super(App, self).__init__(handlers=handlers)


def start_http(port):
    # base.install()
    io_loop = tornado.ioloop.IOLoop.instance()
    application = App()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port)
    io_loop.start()


