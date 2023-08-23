from barladb.classes import Json
from barladb import config
from os import system
import os
import json

RED = "\033[31m"
ORANGE = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"

class BarlaDB:
    def __init__(self):
        self.data = {}

    def get(self, filepath: str):
        try:
            data = Json.get(filepath)
            if config.debug:
                print("BarlaDB: " + GREEN + "Данные успешно были получены!" + RESET)
            if data == {}:
                print("BarlaDB: " + ORANGE + "База данных пустая." + RESET)
                return
            else:
                return data
        except:
            print("BarlaDB: " + RED + f"Базы данных {filepath}.json не существует!" + RESET)
            return
    
    def save(self, filepath: str, data: str):
        try:
            Json.save(filepath, data)
            if config.debug:
                print("BarlaDB: " + GREEN + "Данные успешно были обновлены!" + RESET)
            if data == None:
                print("BarlaDB: " + ORANGE + "Переменная с данными пуста." + RESET)
        except:
            print("BarlaDB: " + RED + f"Базы данных {filepath}.json не существует!" + RESET)
    
    def create(self, filename: str):
        Json.save(filename, self.data)
        if config.debug:
            print("BarlaDB: " + GREEN + f"База данных {filename}.json была успешно создана!" + RESET)
    
    def delete(self, filename: str):
        try:
            os.remove(f"{filename}.json")
            if config.debug:
                print("BarlaDB: " + GREEN + f"База данных {filename}.json была успешно удалена!" + RESET)
        except:
            print("BarlaDB: " + RED + f"Базы данных {filename}.json не существует!" + RESET)
    
    def search(self, filepath: str, key: str):
        try:
            data = Json.get(filepath)
            if data == {}:
                print("BarlaDB: " + ORANGE + "База данных пустая." + RESET)
                return
            if key in data:
                print("BarlaDB: " + GREEN + "Найдено одно совпадение.\n" + RESET + f'"{key}": {data[key]}')
                return data[key]
            else:
                print("BarlaDB: " + ORANGE + "Не найдено ни одно совпадение." + RESET)
                return None
        except:
            print("BarlaDB: " + RED + f"Базы данных {filepath}.json не существует!" + RESET)
            return
    
    def remove_column(self, filepath: str, key: str):
        answer = Json.remove_column(filepath, key)
        if answer:
            print("BarlaDB: " + GREEN + f"Был успешно удален столбец: {key}" + RESET)
        else:
            print("BarlaDB: " + RED + f"Ошибка при удалении столбца: {key}" + RESET)
    
    def columns(self, filepath: str):
        with open(filepath + ".json", "r") as file:
            data = json.load(file)
        int_count = 0
        str_count = 0
        for column in data.values():
            if isinstance(column, (list, tuple, set)):
                for value in column:
                    if isinstance(value, int):
                        int_count += 1
                    elif isinstance(value, str):
                        str_count += 1
            elif isinstance(column, int):
                int_count += 1
            elif isinstance(column, str):
                str_count += 1
        print("BarlaDB: " + GREEN + f"Твоя БД {filepath}.json имеет: {int_count} интенджеров, {str_count} строк" + RESET)
        return int_count, str_count
