from base.service.app_service import BaseApplication
import tornado.ioloop
import tornado.httpserver
from .helloworld import helloworld_grpc
from grpcclient.python import helloworld_pb2_grpc as proto_pb_grpc


class App(BaseApplication):
    def __init__(self):
        handlers = [
            (r'/xing/helloworld1', helloworld_grpc.HelloWorldHandler),
        ]
        super(App, self).__init__(handlers=handlers)


def start_http(port):
    application = App()
    application.register("helloworld", proto_pb_grpc.GreeterStub)
    application.start()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()


