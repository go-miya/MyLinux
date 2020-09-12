import requests
import threading,time
from multiprocessing import Pool
import gevent
import os
import random
import json
def get():
    urls = [
        "http://121.52.235.231:41307/yellowpage_v3/matrix_general/game_mgt/get_real_time_notification_0.1?app_version=2.3.2.10",
        "http://121.52.235.231:41307/yellowpage_v3/matrix_general/game_mgt/get_range_email?user_id=125&nick_name=xx2r&start_num=0&page_count=5&unity_dev=android&channel_code=cn6",
        # "http://121.52.235.231:41227/yellowpage_v3/matrix_general/game_mgt/get_all_notification?token=MTU5OTEyMzI1Ni40Nzp4aW5nOjEyMw==",
        # "http://121.52.235.231:41227/yellowpage_v3/matrix_general/game_mgt/get_all_version?token=MTU5OTEyMzI1Ni40Nzp4aW5nOjEyMw==",
        # "http://121.52.235.231:41227/yellowpage_v3/matrix_general/game_mgt/version_control?app_version=3.5.12.6"
    ]
    s = requests.Session()
    # r = requests.get(random.choice(urls))
    r = s.get(random.choice(urls))
    # print(json.loads(r.text).get("result_code"))
    print(r.headers)
    print(r.content)
    time.sleep(4)


# for i in range(1000):
#     t=threading.Thread(target=run)
#     t.start()

def run(i):
    """
    进程内开启协程，执行解析过程
    :param url_list: 每次进程执行的url数组
    :param i: 进程数
    :return: None
    """
    print("sub-process %s start" % i)
    threads = [gevent.spawn(get) for _ in range(30)]
    gevent.joinall(threads)
    print("sub-process %s end" % i)


def main():
    """
    主进程，为子进程分配任务
    :return:
    """
    print("main process starts >>> pid={}".format(os.getpid()))


    portion = 20

    ps = Pool(portion)
    for i in range(portion):
        ps.apply_async(run, args=(i, ))
    ps.close()
    ps.join()

    print( "main process stoped")

if __name__ == "__main__":
    main()
    # get()