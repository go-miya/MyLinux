import uuid
from base.handler.base_handler import BasicHandler
from base import response_code


class HelloWorld(BasicHandler):

    def pkg(self):
        pkg = {"action": "helloworld"}
        pkg["key"] = str(uuid.uuid4())
        return pkg

    async def get(self):
        pkg = self.pkg()
        try:
            res = await self.service_call(module_name="house", pkg=pkg)
            print(res)
            self.response_return(*response_code.HTTP_OK, res)
        except Exception as e:
            print(e)
            self.err_return(*response_code.SERVER_ERROR)


class HelloWorld1(BasicHandler):

    def pkg(self):
        pkg = {}
        return pkg

    def get(self):
        pkg = self.pkg()
        try:
            res = self.service_call(module_name="house", pkg=pkg)
            self.response_return(*response_code.HTTP_OK, res)
        except:
            self.err_return(*response_code.SERVER_ERROR)
