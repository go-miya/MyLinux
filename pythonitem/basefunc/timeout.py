import time
import signal


class TimeOutError(Exception):
    def __init__(self, msg: str):
        self.msg = msg


def timeOutCallback(error):
	print(error.msg)


def timeOut(interval: int):
    def decorator(func):
        def handler(signum, frame):
            raise TimeOutError("Run func:%s timeout" % func.__name__)

        def wrapper(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(interval)
                res = func(*args, **kwargs)
                signal.alarm(0)
                return res
            except TimeOutError as e:
                timeOutCallback(e)
        return wrapper
    return decorator
