from base.session.base_session import BaseProcessSession
import os
import random
class HouseSession(BaseProcessSession):
    def __init__(self):
        super(HouseSession, self).__init__()

    def call_request(self, pkg):
        print(os.getpid())
        for i in range(5):
            print(i)
        return "HelloWorld %s" % random.random()
