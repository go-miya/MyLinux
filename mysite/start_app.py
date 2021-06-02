from app.helloworld.session import HelloWorldModule

import logging
import os
import sys
import signal
import enviroment
import socket

pids = []


def run(address):
    logging.basicConfig(level=logging.DEBUG)
    logging.info("connect to download stream service")
    HelloWorldModule().start(address)


def main():
    # logging.info(socket.gethostbyname(socket.gethostname()))
    enviroment.config_env("http_service")
    for address in enviroment.CONFIG["download_stream_port"]:
        pid = os.fork()
        if pid == 0:
            run(address)
            return
        else:
            pids.append(pid)
    print(pids)
    signal.signal(signal.SIGTERM, stop_handler)
    signal.signal(signal.SIGINT, stop_handler)
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
    for pid in pids:
        os.kill(pid, signal.SIGTERM)


def trigger_source_stat_handler(signum, frame):
    logging.info("Trigger source stat.")
    for pid in pids:
        logging.info('trigger pid %s' % pid)
        os.kill(pid, signal.SIGUSR1)


if __name__ == "__main__":
    main()
   # http_service.start_http(9999)
