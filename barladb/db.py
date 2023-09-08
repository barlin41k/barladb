from barladb.classes import Json
from barladb.log_functions import Log
from barladb import config
from typing import Union, Any
from os import system
from datetime import datetime
import os
import json

RED = "\033[31m"
ORANGE = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"

class BarlaDB:
    def __init__(self):
        self.data = {}

    def get(self, filepath: str) -> dict:
        try:
            data = Json.get(filepath)
            if config.debug:
                print("BarlaDB: " + GREEN + "Данные успешно были получены!" + RESET)
            if config.log:
                Log.enter_log(f"Данные {filepath}.json успешно были получены")
            if data == {}:
                print("BarlaDB: " + ORANGE + "База данных пустая." + RESET)
                if config.log:
                    Log.enter_log(f"База данных {filepath}.json пуста")
                return
            else:
                return data
        except Exception as e:
            #print(e)
            raise FileNotFoundError(f"Базы данных {filepath}.json не существует!")
            if config.log:
                Log.enter_log(f"Базы данных {filepath}.json не существует")
            return
    
    def save(self, filepath: str, data: str, CreateBackup=(False, False)) -> str:
        try:
            create, return_name = CreateBackup
            backup_name = None
            if create:
                backupData = Json.get(filepath)
                if not os.path.exists("barladb_backups"):
                    os.makedirs("barladb_backups")
                    current_time = datetime.now()
                    backup_time = current_time.strftime("%d.%m.%y")
                    if not os.path.exists(f"barladb_backups/{backup_time}"):
                        os.makedirs(f"barladb_backups/{backup_time}")
                        current_time = datetime.now()
                        backup_time1 = current_time.strftime("%H-%M.%S, %d.%m.%y")
                        backup_name = f"barladb_backups/{backup_time}/{filepath}_backup_{backup_time1}.json"
                        with open(backup_name, "w") as backup:
                            json.dump(data, backup, ensure_ascii=True, indent=2)
                    else:
                        current_time = datetime.now()
                        backup_time1 = current_time.strftime("%H-%M.%S, %d.%m.%y")
                        backup_name = f"barladb_backups/{backup_time}/{filepath}_backup_{backup_time1}.json"
                        with open(backup_name, "w") as backup:
                            json.dump(data, backup, ensure_ascii=True, indent=2)
                else:
                    current_time = datetime.now()
                    backup_time = current_time.strftime("%d.%m.%y")
                    if not os.path.exists(f"barladb_backups/{backup_time}"):
                        os.makedirs(f"barladb_backups/{backup_time}")
                        current_time = datetime.now()
                        backup_time1 = current_time.strftime("%H-%M.%S, %d.%m.%y")
                        backup_name = f"barladb_backups/{backup_time}/{filepath}_backup_{backup_time1}.json"
                        with open(backup_name, "w") as backup:
                            json.dump(data, backup, ensure_ascii=True, indent=2)
                    else:
                        current_time = datetime.now()
                        backup_time1 = current_time.strftime("%H-%M.%S, %d.%m.%y")
                        backup_name = f"barladb_backups/{backup_time}/{filepath}_backup_{backup_time1}.json"
                        with open(backup_name, "w") as backup:
                            json.dump(data, backup, ensure_ascii=True, indent=2)
                if config.debug:
                    print("BarlaDB: " + GREEN + "Бэкап успешно сделан!" + RESET)
                if config.log:
                    Log.enter_log("Бэкап успешно сделан")
                    

            Json.save(filepath, data)
            if data is None:
                if config.debug:
                    print("BarlaDB: " + ORANGE + "Переменная с данными пуста." + RESET)
                if config.log:
                    Log.enter_log("Переменная с данными пуста")
            else:
                if config.debug:
                    print("BarlaDB: " + GREEN + "Данные успешно были обновлены!" + RESET)
                if config.log:
                    Log.enter_log(f"Данные {filepath}.json успешно были обновлены")
            if return_name and create:
                return backup_name
        except:
            raise FileNotFoundError(f"Базы данных {filepath}.json не существует!")
            if config.log:
                Log.enter_log(f"Базы данных {filepath}.json не существует")
    
    def create(self, filename: str) -> bool:
        Json.save(filename, self.data)
        if config.debug:
            print("BarlaDB: " + GREEN + f"База данных {filename}.json была успешно создана!" + RESET)
        if config.log:
            Log.enter_log(f"База данных {filepath}.json успешно была создана")
        return True
    
    def delete(self, filename: str) -> bool:
        try:
            os.remove(f"{filename}.json")
            print("BarlaDB: " + GREEN + f"База данных {filename}.json была успешно удалена!" + RESET)
            if config.log:
                Log.enter_log("База данных {filepath}.json успешно была удалена")
            return True
        except:
            raise FileNotFoundError(f"Базы данных {filepath}.json не существует!")
            if config.log:
                Log.enter_log(f"Базы данных {filepath}.json не существует")
            return False
    
    def search(self, filepath: str, key: str) -> str:
        try:
            data = Json.get(filepath)
            if data == {}:
                print("BarlaDB: " + ORANGE + "База данных пустая." + RESET)
                if config.log:
                    Log.enter_log(f"База данных {filepath}.json пустая")
                return None
            if key in data:
                print("BarlaDB: " + GREEN + "Найдено одно совпадение.\n" + RESET + f'"{key}": {data[key]}')
                if config.log:
                    Log.enter_log(f"Найдено одно совпадение. '{key}': {data[key]}")
                return data[key]
            else:
                print("BarlaDB: " + ORANGE + "Не найдено ни одно совпадение." + RESET)
                if config.log:
                    Log.enter_log("Не найдено ни одно совпадение.")
                return None
        except:
            print("BarlaDB: " + RED + f"Базы данных {filepath}.json не существует!" + RESET)
            if config.log:
                Log.enter_log(f"Базы данных {filepath}.json не существует")
            return
    
    def remove_column(self, filepath: str, key: str) -> bool:
        try:
            answer = Json.remove_column(filepath, key)
            if answer:
                print("BarlaDB: " + GREEN + f"Был успешно удален столбец: {key}" + RESET)
                if config.log:
                    Log.enter_log(f"Был успешно удален столбец: {key}")
                return True
            else:
                print("BarlaDB: " + RED + f"Ошибка при удалении столбца: {key}" + RESET)
                if config.log:
                    Log.enter_log(f"Ошибка при удалении столбца: {key}")
                return False
        except:
            raise FileNotFoundError(f"Базы данных {filepath}.json не существует!")
            if config.log:
                Log.enter_log(f"Базы данных {filepath}.json не существует")
            return False
    
    def columns(self, filepath: str) -> int:
        try:
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
            print("BarlaDB: " + GREEN + f"База данных {filepath}.json имеет: {int_count} интенджеров, {str_count} строк" + RESET)
            if config.log:
                Log.enter_log(f"База данных {filepath}.json имеет: {int_count} интенджеров, {str_count} строк")
            return int_count, str_count
        except:
            raise FileNotFoundError(f"Базы данных {filepath}.json не существует!")
            if config.log:
                Log.enter_log(f"Базы данных {filepath}.json не существует")
            return None
    
    def restore_backup(self, BackupFilepath: str, DatabaseFilepath: str, RemoveBackupFile=True) -> bool:
            if os.path.exists(BackupFilepath):
                pass
            else:
                raise FileExistsError(f"Файла бэкапа не существует. ({BackupFilepath})")
                if config.log:
                    Log.enter_log(f"Файла бэкапа не существует. ({BackupFilepath})")
                return False
            if os.path.exists(DatabaseFilepath):
                pass
            else:
                raise FileExistsError(f"Файла базы данных не существует. ({DatabaseFilepath})")
                if config.log:
                    Log.enter_log(f"Файла базы данных не существует. ({DatabaseFilepath})")
                return False
            with open(BackupFilepath, "r") as file:
                BackupData = json.load(file)
            with open(DatabaseFilepath, "w") as file:
                json.dump(BackupData, file, ensure_ascii=True, indent=2)
            print("BarlaDB: " + GREEN + "Успешный возврат до бэкапа!" + RESET)
            if config.log:
                Log.enter_log("Успешный возврат до бэкапа")
            if RemoveBackupFile:
                os.remove(BackupFilepath)
                if config.debug:
                    print("BarlaDB: " + GREEN + "Файл бэкапа успешно удалён!" + RESET)
                if config.log:
                    Log.enter_log("Файл бэкапа успешно удалён")
