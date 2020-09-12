from abc import ABC
import os
from base.base import BasicHandler

class HelloWorld(BasicHandler, ABC):
    def get(self):
        self.write("Hello World")


class SuiBi(BasicHandler, ABC):
    def get(self):
        self.write("Today is rainy")