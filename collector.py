import logging
import os
import time
import yaml
from pygtail import Pygtail

def collect_logs(config_file):
    try:
        with open(config_file, "r") as f:
            config = yaml.safe_load(f)
        sources = config.get("sources", [])
        for source in sources:
            path = source.get("path")
            alias = source.get("alias", path)

            if not os.path.isfile(path):
                continue

            offset_file = f"{path}.offset"
            for line in Pygtail(path, offset_file=offset_file):
                line = line.strip()
                if line:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    logging.info(f"[{timestamp}] [{alias}] {line}")
    except Exception:
        logging.exception("Error while collecting logs:")
