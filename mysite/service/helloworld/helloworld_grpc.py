from base.handler.base_handler import BasicHandler


class HelloWorldHandler(BasicHandler):
    service_name = "HelloWorld"

    async def get(self):
        await super(HelloWorldHandler, self).get()

    def pkg_input(self, pkg):
        pkg.action = pkg.HelloWorld
        pkg.name = "xing"
        # try:
        #     channel = grpc.insecure_channel('localhost:50051')
        #     request = helloworld_pb2.HelloRequest(name='you')
        #     stub = helloworld_pb2_grpc.GreeterStub(channel)
        #     # response = await stub.ServiceCall(request)
        #     response = await IOLoop.current().run_in_executor(None, stub.ServiceCall, request)
        #     channel.close()
        #     self.response_return(*response_code.HTTP_OK, response.message)
        # except Exception as e:
        #     print(e)
        #     self.err_return(*response_code.SERVER_ERROR)



