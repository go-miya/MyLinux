import logging
from grpcclient.python.helloworld_pb2_grpc import add_GreeterServicer_to_server
from grpcclient.python import helloworld_pb2 as proto_pb
import grpc
from concurrent import futures
import time
from base import response_code
from base.session.base_session import Session


class HelloWorldSession(Session):

    def __init__(self):
        super(HelloWorldSession, self).__init__()

    def on_srv_call_HelloWorldRequest(self, pkg, context=None):
        logging.info('srv call module on_srv_call_HelloWorldRequest. pkg: %s', pkg)
        time.sleep(0.2)
        res = proto_pb.HelloReply()
        res.err_code, res.err_msg = response_code.HTTP_OK
        res.result = "Hello, %s" % pkg.name
        return res


class HelloWorldModule:

    def start(self, address):
        servicer = HelloWorldSession()
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
        add_GreeterServicer_to_server(servicer, server)
        server.add_insecure_port(address)  # '[::]:50051'
        server.start()
        server.wait_for_termination()
