
from tornado.web import RequestHandler
from ..session.schedule import ScheduleSession


class BasicHandler(RequestHandler):
    def __init__(self, application, reqeust, **kwargs):
        super(BasicHandler, self).__init__(application, reqeust, **kwargs)
        self.session = ScheduleSession()
        self.service_call = self.session.service_call

    def pkg(self):
        """rewrite this method"""
        raise NotImplementedError

    def response_return(self, res):
        pass

    def err_return(self, code, err_msg):
        pass

