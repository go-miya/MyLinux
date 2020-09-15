from base.session.base_session import BaseProcessSession
import os
import random
import time
class HouseSession(BaseProcessSession):
    def __init__(self):
        super(HouseSession, self).__init__()

    def call_request(self, pkg):
        print(os.getpid())
        time.sleep(3)
        return "HelloWorld %s" % random.random()
