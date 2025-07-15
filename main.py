from collector import load_config, collect_logs

if __name__ == "__main__":
    config = load_config()
    collect_logs(config)