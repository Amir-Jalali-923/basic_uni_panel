import json


def read_json(file_path: str) -> dict:
    # Read and return JSON data from a file
    with open(file_path, "r") as f:
        return json.load(f)


def write_json(file_path: str, data: dict) -> None:
    # Write dictionary data to a JSON file in readable format
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def append_student(student_id, student_data):
    # Load existing students data, or create empty storage if file is missing/corrupted
    try:
        with open("./data/students.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    # Add new student using the generated ID
    data[student_id] = student_data

    # Save updated students data back to file
    with open("./data/students.json", "w") as f:
        json.dump(data, f, indent=4)


def get_last_id():
    # Read persistent state that tracks the last assigned student ID
    try:
        with open("./data/state.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"last_id": 0}

    # Retrieve current ID, then increment and store it
    last_id = data["last_id"]
    data["last_id"] += 1

    with open("./data/state.json", "w") as f:
        json.dump(data, f, indent=4)

    return last_id
