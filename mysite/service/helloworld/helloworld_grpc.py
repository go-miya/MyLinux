import logging

from base.handler.base_handler import BasicHandler


class HelloWorldHandler(BasicHandler):
    service_name = "HelloWorld"

    async def get(self):
        await super(HelloWorldHandler, self).get()

    def pkg_input(self, pkg):
        pkg.action = pkg.HelloWorld
        pkg.name = "xing"


