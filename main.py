import daemon
import logging
import os
import time
from collector import collect_logs

LOG_FILE = "/var/log/kcollect/collector.log"
CONFIG_FILE = "/opt/kcollect/config.yaml"

def setup_logging():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

def run():
    setup_logging()
    logging.info("Daemon started.")
    try:
        while True:
            collect_logs(CONFIG_FILE)
            time.sleep(5)
    except Exception:
        logging.exception("Daemon crashed.")
    finally:
        logging.info("Daemon stopped.")

if __name__ == "__main__":
    setup_logging()
    with daemon.DaemonContext(
        working_directory="/opt/kcollect",
        umask=0o022,
        stdout=None,
        stderr=None,
    ):
        run()
