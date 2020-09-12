import logging
from service import http_service
import os
import sys
import signal
import enviroment


def run(port):
    logging.basicConfig(level=logging.NOTSET)
    logging.info("connect to rout, start service")
    http_service.start_http(port)


pids = []
def main():
    enviroment.config_env("http_service")
    for i in range(3):
        pid = os.fork()
        if pid == 0:
            run(enviroment.CONFIG["start_hostids"][i])
            return
        else:
            pids.append(pid)
    print(pids)
    signal.signal(signal.SIGTERM, stop_handler)
    # signal.signal(signal.SIGINT, stop_handler)
    signal.signal(signal.SIGUSR1, trigger_source_stat_handler)

    while pids:
        try:
            pid, ret = os.wait()
            logging.info('the ret: %d', ret)
            logging.info('the sys.argv %s', sys.argv)
            hid = pids[pid]
            del pids[pid]
            if ret > 0:
                logging.error("http process %d died accidentally!", hid)
        except:
            pass

def stop_handler(signum, frame):
    logging.info("Shutdown http service.")
    for pid in pids.keys():
        os.kill(pid, signal.SIGTERM)

def trigger_source_stat_handler(signum, frame):
    logging.info("Trigger source stat.")
    for pid in pids.keys():
        logging.info('trigger pid %s' % pid)
        os.kill(pid, signal.SIGUSR1)

if __name__ == "__main__":
    main()

