import daemon
import logging
import time
import os

LOG_FILE = "/var/log/kcollect.log"

def setup_logging():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
    )

def run():
    setup_logging()
    logging.info("Daemon started successfully.")
    try:
        while True:
            logging.info("Daemon is alive.")
            time.sleep(10)
    except Exception as e:
        logging.exception("Exception in daemon:")
    finally:
        logging.info("Daemon exiting.")

if __name__ == "__main__":
    with daemon.DaemonContext():
        run()