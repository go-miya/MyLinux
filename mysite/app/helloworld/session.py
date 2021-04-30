import asyncio

from grpcclient.python.helloworld_pb2_grpc import GreeterServicer, add_GreeterServicer_to_server
from grpcclient.python.helloworld_pb2 import HelloReply
import grpc
from concurrent import futures
import time
from tornado.ioloop import IOLoop


class Session(GreeterServicer):

    def ServiceCall(self, request, context):
        return self.on_srv_call_HelloWorldRequest(request, context)


class HelloWorldSession(Session):

    def __init__(self):
        super(HelloWorldSession, self).__init__()

    def on_srv_call_HelloWorldRequest(self, request, context=None):
        # await IOLoop.current().run_in_executor(None, asyncio.sleep, 0.5)
        time.sleep(0.2)
        return HelloReply(message="Hello,%s" % request.name)


class HelloWorldModule:

    def start(self):
        servicer = HelloWorldSession()
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
        add_GreeterServicer_to_server(servicer, server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()
