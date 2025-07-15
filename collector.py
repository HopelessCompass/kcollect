import os
import yaml
import json
from datetime import datetime

STATE_FILE = "state.json"

def load_config(path='config.yaml'):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def load_state():
    if os.path.isfile(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

def collect_logs(config):
    output_dir = config['output_directory']
    os.makedirs(output_dir, exist_ok=True)

    state = load_state()

    out_file_path = os.path.join(output_dir, f"collected_{datetime.now().date()}.log")
    with open(out_file_path, 'a') as out_file:
        for source in config['log_sources']:
            name = source['name']
            path = source['path']

            if not os.path.isfile(path):
                print(f"⚠️ Файл {path} не найден, пропускаем...")
                continue

            last_pos = state.get(path, 0)

            try:
                with open(path, 'r', errors='ignore') as log_file:
                    log_file.seek(last_pos)
                    for line in log_file:
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        tagged_line = f"[{timestamp}] [{name}:{path}] {line}"
                        out_file.write(tagged_line)

                    state[path] = log_file.tell()
            except Exception as e:
                print(f"⚠️ Ошибка при чтении {path}: {e}")

    save_state(state)
    print(f"✅ Логи собраны в {out_file_path}")