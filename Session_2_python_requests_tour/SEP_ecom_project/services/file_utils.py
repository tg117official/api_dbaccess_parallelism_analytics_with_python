# services/file_utils.py
import json
import os

def load_json(filepath):
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []  # fallback for empty or broken JSON


def write_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
