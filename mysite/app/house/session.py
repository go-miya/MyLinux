from base.session.base_session import BaseProcessSession
from base.redisfunc.rediscon import RedisPool
import os
import random
import uuid
import json


class HouseSession(BaseProcessSession):
    def __init__(self):
        self.queue = "queue"
        super(HouseSession, self).__init__()

    def call_request(self, pkg):
        print(os.getpid())
        pkg["id"] = str(uuid.uuid4())
        self.write_to_middle_part(pkg)
        return self.get_from_middle_part(pkg["id"])
        # return "HelloWorld %s" % random.random()

    def write_to_middle_part(self, pkg):
        print("add task to queue")
        self.redis_conn.lpush(self.queue, json.dumps(pkg))
        print(self.redis_conn.lrange(self.queue, 0, -1))
        print("add task finished")    

    def get_from_middle_part(self, id):
        return self.redis_conn.brpop(id, timeout=2)
        

