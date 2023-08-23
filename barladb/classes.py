import json
RED = "\033[31m"
ORANGE = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"

class Json:
    @staticmethod
    def get(filepath: str):
        with open(filepath + ".json", "r") as file:
            return json.load(file)
    @staticmethod
    def save(filepath: str, data: str):
        with open(filepath + ".json", "w") as file:
            json.dump(data, file, ensure_ascii=True, indent=2)
    @staticmethod
    def remove_column(filepath: str, key: str):
        try:
            with open(filepath + ".json", "r") as file:
                data = json.load(file)
            if key in data:
                del data[key]
                with open(filepath + ".json", "w") as file:
                    json.dump(data, file, ensure_ascii=True, indent=2)
                return True
            else:
                return False
        except:
            print("BarlaDB: " + RED + f"Базы данных {filepath}.json не существует!" + RESET)
