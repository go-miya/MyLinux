from abc import ABCMeta, abstractmethod


class BaseSession(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def service_call(self, module_name, pkg):
        pass