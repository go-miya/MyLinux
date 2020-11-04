import time
import signal


class TimeOutError(Exception):
    def __init__(self, msg: str):
        self.msg = msg


def timeOut(interval: int, callback: callable):
    def decorator(func):
        def handler(signum, frame):
            raise TimeOutError("Run func timeout")

        def wrapper(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(interval)
                res = func(*args, **kwargs)
                signal.alarm(0)
                return res
            except TimeOutError as e:
                callback(e, func.__name__)
        return wrapper
    return decorator


def timeOutCallback(e: TimeOutError, name):
    print(e.msg, name)


@timeOut(2, timeOutCallback)
def task1():
    print("task1 start")
    time.sleep(3)
    print("task1 finished")


if __name__ == "__main__":
    task1()