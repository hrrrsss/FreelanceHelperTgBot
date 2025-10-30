from pathlib import Path
import json
from datetime import datetime

DATA_FILE = Path("json_files/user_q.json")

def load_last_requests():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

            return {int(k): datetime.fromisoformat(v) for k, v in data.items()}
    return {}


def save_last_requests(data: dict):
    s = {str(k): v.isoformat() for k, v in data.items()}
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(s, f, ensure_ascii=False, indent=2)