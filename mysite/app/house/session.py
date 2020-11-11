from base.session.base_session import BaseProcessSession
import os
import random
import uuid


class HouseSession(BaseProcessSession):
    def __init__(self):
        super(HouseSession, self).__init__()

    def call_request(self, pkg):
        print(os.getpid())
        for i in range(5):
            print(i)
        return "HelloWorld %s" % random.random()

    def write_to_middle_part(self, pkg):
        pkg["id"] = uuid.uuid4()


    def get_from_middle_part(self, message):
        pass

