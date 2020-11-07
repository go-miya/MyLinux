from base.session.base_session import BaseProcessSession
import os
import random
import time
class HouseSession(BaseProcessSession):
    def __init__(self):
        super(HouseSession, self).__init__()

   async def call_request(self, pkg):
        print(os.getpid())
        for i in range(5):
            print(i)
           await gen.sleep(1)
        return "HelloWorld %s" % random.random()
