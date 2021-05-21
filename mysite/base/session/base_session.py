import logging
from grpcclient.python.helloworld_pb2_grpc import GreeterServicer


class Session(GreeterServicer):

    def ServiceCall(self, pkg, context):
        logging.debug('get---------%s---%s', pkg, context)
        return self.on_srv_call_request(pkg, context)

    def on_srv_call_request(self, *args, **kwargs):
        raise NotImplementedError
