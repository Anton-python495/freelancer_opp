import json

def save_json(data, filename):
    with open(f"{filename}.json", "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii = False, indent=4)

def load_json(filename):
    with open(f"{filename}.json", "r", encoding = "utf-8") as file:
        loaded_data = json.load(file)
    return loaded_data