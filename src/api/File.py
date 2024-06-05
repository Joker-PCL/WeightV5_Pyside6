import json
import os


class File():
    def __init__(self, jsonFile):
        self.jsonFile = jsonFile

    def read(self):
        try:
            with open(self.jsonFile, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return {}

    def write(self, data):
        with open(self.jsonFile, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def append(self, data):
        existing_data = self.read()
        if not existing_data:
            existing_data = []
        elif not isinstance(existing_data, list):
            existing_data = [existing_data]
        
        existing_data.append(data)
        self.write(existing_data)

    def clear(self):
        with open(self.jsonFile, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=4)

    def delete(self):
        try:
            os.remove(self.jsonFile)
        except FileNotFoundError:
            return None
