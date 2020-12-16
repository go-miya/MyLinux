import tornado.ioloop
import threading


class HandlerService:
    def __init__(self):
        self.ioloop = tornado.ioloop.IOLoop.instance()
        self.ioloop.service = self

        self.callback_to_main_thread = self.ioloop.add_callback
        self._thread = threading.Thread(target=self.loop)

    def loop(self):
        pass

