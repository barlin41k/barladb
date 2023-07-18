from barladb.classes import Json
from barladb import config
from os import system
import os
import json
try:
    from colorama import Style, Fore, init
except:
    system("pip install colorama")
    from colorama import Style, Fore, init
init()
data = {

}

#get - получить
def get(filepath: str):
    try:
        data = Json.get(filepath)
        if config.debug:
            print("BarlaDB: " + Fore.GREEN + "Данные успешно были получены!" + Style.RESET_ALL)
        if data == {}:
            print("BarlaDB: " + Fore.YELLOW + "База данных пустая." + Style.RESET_ALL)
            return
        else:
            return data
    except:
        print("BarlaDB: " + Fore.RED + f"Базы данных {filepath}.json не существует!" + Style.RESET_ALL)
        return
#save - сохранить в БД
def save(filepath: str, data: str):
    try:
        Json.save(filepath, data)
        if config.debug:
            print("BarlaDB: " + Fore.GREEN + "Данные успешно были обновлены!" + Style.RESET_ALL)
        if data == None:
            print("BarlaDB: " + Fore.YELLOW + "Переменная с данными пуста." + Style.RESET_ALL)
        else:
            return
    except:
        print("BarlaDB: " + Fore.RED + f"Базы данных {filepath}.json не существует!" + Style.RESET_ALL)
        return
#create - создать БД
def create(filename: str):
    Json.save(filename, data)
    if config.debug:
        print("BarlaDB: " + Fore.GREEN + f"База данных {filepath}.json была успешно создана!" + Style.RESET_ALL)
#delete - удалить БД
def delete(filepath: str):
    try:
        os.remove(f"{filename}.json")
        if config.debug:
            print("BarlaDB: " + Fore.GREEN + f"База данных {filepath}.json была успешно удалена!" + Style.RESET_ALL)
        else:
            return data
    except:
        print("BarlaDB: " + Fore.RED + f"Базы данных {filepath}.json не существует!" + Style.RESET_ALL)
        return
#search - парсинг БД на ключ
def search(filepath: str, key: str):
    try:
        with open(filepath + ".json", "r") as file:
            data = Json.get(filepath)
            if data == {}:
                print("BarlaDB: " + Fore.YELLOW + "База данных пустая." + Style.RESET_ALL)
                return
            if key in data:
                print("BarlaDB: " + Fore.GREEN + "Найдено одно совпадение.\n" + Style.RESET_ALL + f'"{key}": {data[key]}')
                return data[key]
            else:
                print("BarlaDB: " + Fore.YELLOW + "Не найдено ни одно совпадение." + Style.RESET_ALL)
                return None
    except:
        print("BarlaDB: " + Fore.RED + f"Базы данных {filepath}.json не существует!" + Style.RESET_ALL)
        return
#remove_columm - удаление столбца по ключу в БД
def remove_column(filepath: str, key: str):
    answer = Json.remove_column(filepath, key)
    if answer:
        print("BarlaDB: " + Fore.GREEN + f"Был успешно удален столбец: {key}" + Style.RESET_ALL)
    else:
        print("BarlaDB: " + Fore.RED + f"Ошибка при удалении столбца: {key}" + Style.RESET_ALL)
#columns - информация о столбцах в БД
def columns(filepath: str):
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
    print("BarlaDB: " + Fore.GREEN + f"Твоя БД {filepath}.json имеет: {int_count} ints, {str_count} str" + Style.RESET_ALL)
    return int_count, str_count