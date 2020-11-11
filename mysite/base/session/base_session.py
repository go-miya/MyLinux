from abc import ABCMeta, abstractmethod


class BaseScheduleSession(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def service_call(self, module_name, pkg):
        pass


class BaseProcessSession(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def call_request(self, pkg):
        pass

    @abstractmethod
    def write_to_middle_part(self, message):
        pass

    @abstractmethod
    def get_from_middle_part(self, message):
        pass