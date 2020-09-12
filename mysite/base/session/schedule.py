from .base_session import BaseSession
import typing

class ScheduleSession(BaseSession):

    def __init__(self):
        super(ScheduleSession, self).__init__()

    def service_call(self, module_name: str, pkg: typing.Dict):
        pass