import os
import json

REPORT_DIR = "reports"


def ensure_report_dir():
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)


def save_json(filename, data):
    ensure_report_dir()

    path = os.path.join(REPORT_DIR, filename)

    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def save_markdown(filename, content):
    ensure_report_dir()

    path = os.path.join(REPORT_DIR, filename)

    with open(path, "w") as f:
        f.write(content)