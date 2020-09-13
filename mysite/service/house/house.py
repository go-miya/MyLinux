from base.handler.base_handler import BasicHandler
from base import response_code
import time


class HelloWorld(BasicHandler):

    def pkg(self):
        pkg = {}
        return pkg

    def get(self):
        pkg = self.pkg()
        try:
            time.sleep(10)
            print("this is helloworld")
            res = self.service_call(module_name="house", pkg=pkg)
            self.response_return(*response_code.HTTP_OK, res)
        except:
            self.err_return(*response_code.SERVER_ERROR)


class HelloWorld1(BasicHandler):

    def pkg(self):
        pkg = {}
        return pkg

    def get(self):
        pkg = self.pkg()
        try:
            print("this is helloworld11111")
            res = self.service_call(module_name="house", pkg=pkg)
            self.response_return(*response_code.HTTP_OK, res)
        except:
            self.err_return(*response_code.SERVER_ERROR)
