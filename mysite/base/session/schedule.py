from .base_session import BaseScheduleSession
import typing


class ScheduleSession(BaseScheduleSession):

    def __init__(self):
        super(ScheduleSession, self).__init__()

    def service_call(self, module_name: str, pkg: typing.Dict):
        return "welcome"