from abc import ABC

from tornado.web import RequestHandler


class BasicHandler(RequestHandler, ABC):
    def __init__(self, application, reqeust, **kwargs):
        super(BasicHandler, self).__init__(application, reqeust, **kwargs)
