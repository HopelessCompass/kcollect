import logging
import os
import time
import yaml
from pygtail import Pygtail

OFFSET_DIR = "/opt/kcollect/offsets"

def collect_logs(config_file):
    try:
        logging.debug(f"Loading config from {config_file}")
        with open(config_file, "r") as f:
            config = yaml.safe_load(f)

        sources = config.get("sources", [])
        logging.debug(f"Configured sources: {sources}")

        for source in sources:
            path = source.get("path")
            alias = source.get("alias", path)
            logging.debug(f"Processing source: path={path}, alias={alias}")

            if not os.path.isfile(path):
                logging.warning(f"Log file does not exist or is not a file: {path}")
                continue

            safe_name = path.replace("/", "_").lstrip("_") + ".offset"
            offset_file = os.path.join(OFFSET_DIR, safe_name)

            lines_read = 0
            for line in Pygtail(path, offset_file=offset_file):
                line = line.strip()
                if line:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    logging.info(f"[{timestamp}] [{alias}] {line}")
                    lines_read += 1
            logging.debug(f"Read {lines_read} new lines from {path} using offset file {offset_file}")
    except Exception:
        logging.exception("Error while collecting logs:")
