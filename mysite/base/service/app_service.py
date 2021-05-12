import logging

from tornado.web import Application
import grpc
from enviroment import CONFIG


class BaseApplication(Application):
    def __init__(self, handlers=None, default_host=None, transforms=None, **settings):
        self._stubs = []
        super(BaseApplication, self).__init__(
            handlers=handlers, default_host=default_host, transforms=transforms, settings=settings)

    def register(self, service_name: str, stub: callable, *args, **kwargs):
        self._stubs.append((service_name, stub))

    def register_grpb_stub_with_channel(self, name: str, stub: callable):
        if not hasattr(self, "_grpc_channel"):
            self._grpc_channel = create_channel()
            self._grpc_stubs = {}
        self._grpc_stubs[name] = create_grpc_stub(stub, self._grpc_channel)

    def start(self):
        logging.info("Web service start")
        for service_name, stub in self._stubs:
            self.register_grpb_stub_with_channel(service_name, stub)


def create_channel():
    channel = grpc.insecure_channel(CONFIG.get("download_stream_port"))
    return channel


def create_grpc_stub(stub: callable, channel: grpc.insecure_channel):
    return stub(channel)
