import logging
from grpcclient.python.helloworld_pb2_grpc import add_GreeterServicer_to_server
from grpcclient.python import helloworld_pb2 as proto_pb
import grpc
from concurrent import futures
import time
from base import response_code
from base.session.base_session import Session
from .dispatcher import tasks


class HelloWorldSession(Session):

    def __init__(self):
        super(HelloWorldSession, self).__init__()

    def on_srv_call_request(self, pkg, context=None):
        logging.info('srv call module on_srv_call_request: %s', pkg.action)
        time1 = time.time()
        res = proto_pb.HelloReply()
        try:
            result = tasks.get(pkg.action)(pkg)
            res.err_code, res.err_msg = response_code.HTTP_OK
            res.result = result
        except Exception as e:
            res.err_code, res.err_msg, _ = response_code.SERVER_ERROR
            res.result = ""
        finally:
            logging.info('%s on_srv_call_request spend_time:%s',
                         pkg.action, time.time() - time1)
            return res


class HelloWorldModule:

    def start(self, address):
        servicer = HelloWorldSession()
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
        add_GreeterServicer_to_server(servicer, server)
        server.add_insecure_port(address)  # '[::]:50051'
        server.start()
        server.wait_for_termination()
