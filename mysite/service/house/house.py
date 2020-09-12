from abc import ABC
from base.handler.base_handler import BasicHandler
from base import response_code

class HelloWorld(BasicHandler, ABC):

    def pkg(self):
        pkg = {}
        return pkg

    def get(self):
        pkg = self.pkg()
        try:
            res = self.service_call(module_name="house", pkg=pkg)
            self.response_return(res)
        except:
            self.err_return(*response_code.TIME_OUT_ERROR)