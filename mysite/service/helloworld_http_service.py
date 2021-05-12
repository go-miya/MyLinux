from base.service.app_service import BaseApplication
import tornado.ioloop
import tornado.httpserver
from .house import house
from .helloworld import helloworld_grpc
from grpcclient.python import helloworld_pb2_grpc as proto_pb_grpc, helloworld_pb2 as proto_pb
# from base import base


class App(BaseApplication):
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
    application.register("helloworld", proto_pb_grpc.GreeterStub)
    application.start()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port)
    io_loop.start()


