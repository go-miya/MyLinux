from abc import ABCMeta, abstractmethod


class BaseScheduleSession(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def service_call(self, module_name, pkg):
        pass


class BaseProcessSession(metaclass=ABCMeta):
    def __init__(self, service):
        pass

    @abstractmethod
    def call_request(self, pkg):
        pass