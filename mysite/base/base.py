
import tornado.platform.asyncio
import tornado.web
import greenlet
from base.service.handler_service import HandlerService

class BaseIoloop(tornado.platform.asyncio.AsyncIOLoop):
    def __init__(self):
        super(BaseIoloop, self).__init__()
        self.loop_greenlet = greenlet.greenlet(super(BaseIoloop, self).start())

    def start(self) -> None:
        # self.service.start()
        self.loop_greenlet.switch()

def install():
    ioloop = BaseIoloop()
    ioloop.install()


class Application(tornado.web.Application):
    def __init__(self, handlers=None, default_host="", transforms=None, wsgi=False, **settings):
        tornado.web.Application.__init__(self, handlers, default_host, transforms, wsgi=wsgi, **settings)
        self.service = HandlerService()
