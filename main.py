import time
import signal
import sys
import daemon
from collector import load_config, collect_logs

RUNNING = True

def handle_exit(signum, frame):
    global RUNNING
    RUNNING = False
    print("⛔ Получен сигнал завершения, выходим...")

def run_daemon(interval_seconds=30):
    config = load_config()

    signal.signal(signal.SIGTERM, handle_exit)
    signal.signal(signal.SIGINT, handle_exit)

    while RUNNING:
        collect_logs(config)
        time.sleep(interval_seconds)

if __name__ == "__main__":
    with daemon.DaemonContext():
        run_daemon()
