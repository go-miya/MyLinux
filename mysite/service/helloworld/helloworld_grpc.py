from base.handler.base_handler import BasicHandler
from base import response_code
from grpcclient.python import helloworld_pb2_grpc, helloworld_pb2
import grpc
from tornado.ioloop import IOLoop


class HelloWorldHandler(BasicHandler):

    async def get(self):
        print(self.get_argument("token", None))
        try:
            channel = grpc.insecure_channel('localhost:50051')
            request = helloworld_pb2.HelloRequest(name='you')
            stub = helloworld_pb2_grpc.GreeterStub(channel)
            # response = await stub.ServiceCall(request)
            response = await IOLoop.current().run_in_executor(None, stub.ServiceCall, request)
            channel.close()
            self.response_return(*response_code.HTTP_OK, response.message)
        except Exception as e:
            print(e)
            self.err_return(*response_code.SERVER_ERROR)



