import typing
from tornado.web import RequestHandler
from ..session.schedule import ScheduleSession
import logging


class BasicHandler(RequestHandler):
    def __init__(self, application, reqeust, **kwargs):
        super(BasicHandler, self).__init__(application, reqeust, **kwargs)
        print(application)
        self.session = ScheduleSession()
        self.service_call = self.session.service_call
        self.content_type = "json"

    def pkg(self):
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

    def err_return(self, code: int, err_msg: str):
        logging.debug(f"err code is: {code}", f"err msg is: {err_msg}")
        self.response_return(code, err_msg)

