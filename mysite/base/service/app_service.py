import logging

from tornado.web import Application
import grpc
from enviroment import CONFIG
from collections import deque


class BaseApplication(Application):
    """
    base app class
    """
    def __init__(self, handlers=None, default_host=None, transforms=None, **settings):
        """
        self._stubs saves a 'service_name' and a 'grpc stub'
        :param handlers:
        :param default_host:
        :param transforms:
        :param settings:
        """
        self._stubs = []
        super(BaseApplication, self).__init__(
            handlers=handlers, default_host=default_host, transforms=transforms, settings=settings)

    def register(self, service_name: str, stub: callable, *args, **kwargs):
        """
        Add a (service_name, grpc_stub) to self._stubs
        :param service_name:
        :param stub:
        :param args:
        :param kwargs:
        :return:
        """
        self._stubs.append((service_name, stub))

    def register_grpb_stub_with_channel(self, name: str, stub: callable):
        """
        bind service_nam and grpc_stub
        :param name:
        :param stub:
        :return:
        """
        if not hasattr(self, "_grpc_channel"):
            self._grpc_channels = create_channel()
            self._grpc_stubs = {}
        self._grpc_stubs[name] = create_grpc_stub(stub, self._grpc_channels)

    def start(self):
        logging.info("Web service start")
        for service_name, stub in self._stubs:
            self.register_grpb_stub_with_channel(service_name, stub)


def create_channel():
    """
    create grpc channel
    :return:
    """
    channels = [grpc.insecure_channel(address) for address in CONFIG.get("download_stream_port")]
    return channels


def create_grpc_stub(stub: callable, channels: [grpc.insecure_channel]):
    """
    bind grpc_stub with grpc_channel
    :param stub:
    :param channels:
    :return:
    """
    grpc_stub_deque = deque()
    for channel in channels:
        grpc_stub_deque.append(stub(channel))
    return grpc_stub_deque
