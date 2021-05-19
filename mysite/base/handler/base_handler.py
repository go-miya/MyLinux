import collections
import typing
from abc import ABC
from tornado.web import RequestHandler
from grpcclient.python import helloworld_pb2 as proto_pb
from base import response_code
from tornado.ioloop import IOLoop
import logging


class BaseHandler(RequestHandler, ABC):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        for name, grpc_stub_lists in application._grpc_stubs.items():
            setattr(self, name, grpc_stub_lists)

    def get_grpc_stub(self, name: str):
        grpc_stub_deque: collections.deque = getattr(self, name.lower())
        logging.info("called grpc_stub_lists: %s " % grpc_stub_deque)
        grpc_stub = grpc_stub_deque.pop()
        grpc_stub_deque.appendleft(grpc_stub)
        return grpc_stub

    async def _service_call(self, service_name, package=None, timeout=None, **kwargs):
        logging.info("{}:{}".format(service_name, package.action))
        try:
            stub = self.get_grpc_stub(service_name)
            logging.info("call stub: %s" % id(stub))
            response = await IOLoop.current().run_in_executor(None, stub.ServiceCall, package)
            return response
        except Exception as e:
            logging.error(e, exc_info=True)
            self.response_return(*response_code.SERVER_ERROR)

    def response_return(self, *args, **kwargs):
        raise NotImplementedError


class BasicHandler(BaseHandler, ABC):

    service_name = None

    def __init__(self, application, reqeust, **kwargs):
        super(BasicHandler, self).__init__(application, reqeust, **kwargs)
        self.content_type = "json"

    async def get(self):
        try:
            pkg = proto_pb.HelloRequest()
            self.pkg_input(pkg)
        except Exception as ex:
            logging.error('pkg input error: {}'.format(repr(ex)), exc_info=True)
            self.response_return(400, "pkg_error", {})
            return
        try:
            res = await self._service_call(self.service_name, pkg, timeout=1)
            self.response_return(*response_code.HTTP_OK, res.result)
        except Exception as ex:
            logging.error('call service error: {}'.format(repr(ex)), exc_info=True)
            self.response_return(*response_code.SERVER_ERROR)

    def pkg_input(self, pkg):
        raise NotImplementedError

    def pkg_post(self, pkg):
        raise NotImplementedError

    def init_pkg(self):
        """rewrite this method"""
        raise NotImplementedError

    def response_return(self, code: int, msg: str,  res: typing.Dict = None):
        ret = {
            "code": code,
            "msg": msg,
            "result": res
        }
        self.set_status(code)
        self.set_header("Content-Type", "application/json")
        self.write(ret)

