from .base_session import BaseScheduleSession
import typing
import importlib


class ScheduleSession(BaseScheduleSession):

    def __init__(self):
        super(ScheduleSession, self).__init__()

    def service_call(self, module_name: str, pkg: typing.Dict):
        imported_module_name = "app.%s.session" % module_name
        module = importlib.import_module(imported_module_name)
        obj = getattr(module, module_name.capitalize() + "Session")
        return obj().call_request(pkg)

