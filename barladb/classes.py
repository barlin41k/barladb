import json
try:
    from colorama import Style, Fore, init
except:
    system("pip install colorama")
    from colorama import Style, Fore, init
init()

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
            print("BarlaDB: " + Fore.RED + f"Базы данных {filepath}.json не существует!" + Style.RESET_ALL)