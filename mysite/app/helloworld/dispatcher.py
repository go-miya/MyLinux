from grpcclient.python import helloworld_pb2 as proto_pb

tasks = {}
TASK_PROTO = proto_pb.HelloRequest()


def wrapper(action):
    def dec(func):
        tasks[action] = func

        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        return inner
    return dec


@wrapper(TASK_PROTO.HelloWorld)
def helloworld(pkg):
    res = "hello %s" % pkg.name
    return res
