from base.session.base_session import BaseProcessSession


class HouseSession(BaseProcessSession):
    def __init__(self):
        super(HouseSession, self).__init__()

    def call_request(self, pkg):
        pass