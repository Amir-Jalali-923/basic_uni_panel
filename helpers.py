import json
import os

def read_json(file_path: str) -> dict:
    with open(file_path, "r") as f:
        return json.load(f)
    
def write_json(file_path: str, data: dict) -> None:
    with open(file_path, "w") as f:
        json.dump(data, f)

import json

def append_student(student_id, student_data):
    try:
        with open("./data/students.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data[student_id] = student_data

    with open("./data/students.json", "w") as f:
        json.dump(data, f, indent=4)

def get_last_id():
    try:
        with open("./data/state.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"last_id": 0}

    last_id = data["last_id"]
    with open("./data/state.json", "w") as f:
        data["last_id"] += 1
        json.dump(data, f, indent=4)

    return last_id