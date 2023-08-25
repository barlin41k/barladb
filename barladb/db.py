from barladb.classes import Json
from barladb import config
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

    def get(self, filepath: str):
        try:
            data = Json.get(filepath)
            if config.debug:
                print("BarlaDB: " + GREEN + "Данные успешно были получены!" + RESET)
                if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: Данные {filepath}.json успешно были получены\n")
                        else:
                            log.write(f"\n{log_time}: Данные {filepath}.json успешно были получены")
            if data == {}:
                print("BarlaDB: " + ORANGE + "База данных пустая." + RESET)
                if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: База данных {filepath}.json пуста\n")
                        else:
                            log.write(f"\n{log_time}: База данных {filepath}.json пуста")
                return
            else:
                return data
        except:
            print("BarlaDB: " + RED + f"Базы данных {filepath}.json не существует!" + RESET)
            if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: Базы данных {filepath}.json не существует\n")
                        else:
                            log.write(f"\n{log_time}: Базы данных {filepath}.json не существует")
            return
    
    def save(self, filepath: str, data: str, CreateBackup=(False, False)):
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
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: Бэкап успешно сделан\n")
                        else:
                            log.write(f"\n{log_time}: Бэкап успешно сделан")
                if return_name and create:
                    return backup_name

            Json.save(filepath, data)
            if config.debug:
                print("BarlaDB: " + GREEN + "Данные успешно были обновлены!" + RESET)
                if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: Данные {filepath}.json успешно были обновлены\n")
                        else:
                            log.write(f"\n{log_time}: Данные {filepath}.json успешно были обновлены")
            if data is None:
                print("BarlaDB: " + ORANGE + "Переменная с данными пуста." + RESET)
                if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: Переменная с данными пуста\n")
                        else:
                            log.write(f"\n{log_time}: Переменная с данными пуста")
        except:
            print("BarlaDB: " + RED + f"Базы данных {filepath}.json не существует!" + RESET)
            if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: Базы данных {filepath}.json не существует\n")
                        else:
                            log.write(f"\n{log_time}: Базы данных {filepath}.json не существует")
    
    def create(self, filename: str):
        Json.save(filename, self.data)
        if config.debug:
            print("BarlaDB: " + GREEN + f"База данных {filename}.json была успешно создана!" + RESET)
            if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: База данных {filepath}.json успешно была создана\n")
                        else:
                            log.write(f"\n{log_time}: База данных {filepath}.json успешно была создана")
    
    def delete(self, filename: str):
        try:
            os.remove(f"{filename}.json")
            if config.debug:
                print("BarlaDB: " + GREEN + f"База данных {filename}.json была успешно удалена!" + RESET)
            if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: База данных {filepath}.json успешно была удалена\n")
                        else:
                            log.write(f"\n{log_time}: База данных {filepath}.json успешно была удалена")
        except:
            print("BarlaDB: " + RED + f"Базы данных {filename}.json не существует!" + RESET)
            if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: Базы данных {filepath}.json не существует\n")
                        else:
                            log.write(f"\n{log_time}: Базы данных {filepath}.json не существует")
    
    def search(self, filepath: str, key: str):
        try:
            data = Json.get(filepath)
            if data == {}:
                print("BarlaDB: " + ORANGE + "База данных пустая." + RESET)
                if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: База данных {filepath}.json пустая\n")
                        else:
                            log.write(f"\n{log_time}: База данных {filepath}.json пустая")
                return
            if key in data:
                print("BarlaDB: " + GREEN + "Найдено одно совпадение.\n" + RESET + f'"{key}": {data[key]}')
                if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: Найдено одно совпадение. '{key}': {data[key]}\n")
                        else:
                            log.write(f"\n{log_time}: Найдено одно совпадение. '{key}': {data[key]}")
                return data[key]
            else:
                print("BarlaDB: " + ORANGE + "Не найдено ни одно совпадение." + RESET)
                if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: Не найдено ни одно совпадение.\n")
                        else:
                            log.write(f"\n{log_time}: Не найдено ни одно совпадение.")
                return None
        except:
            print("BarlaDB: " + RED + f"Базы данных {filepath}.json не существует!" + RESET)
            if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: Базы данных {filepath}.json не существует\n")
                        else:
                            log.write(f"\n{log_time}: Базы данных {filepath}.json не существует")
            return
    
    def remove_column(self, filepath: str, key: str):
        answer = Json.remove_column(filepath, key)
        try:
            if answer:
                print("BarlaDB: " + GREEN + f"Был успешно удален столбец: {key}" + RESET)
                if config.log:
                        current_time = datetime.now()
                        name = current_time.strftime("%d.%m.%y")
                        log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                        with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                            if not log.read():
                                log.write(f"{log_time}: Был успешно удален столбец: {key}\n")
                            else:
                                log.write(f"\n{log_time}: Был успешно удален столбец: {key}")
            else:
                print("BarlaDB: " + RED + f"Ошибка при удалении столбца: {key}" + RESET)
                if config.log:
                        current_time = datetime.now()
                        name = current_time.strftime("%d.%m.%y")
                        log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                        with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                            if not log.read():
                                log.write(f"{log_time}: Ошибка при удалении столбца: {key}\n")
                            else:
                                log.write(f"\n{log_time}: Ошибка при удалении столбца: {key}")
        except:
            print("BarlaDB: " + RED + f"Базы данных {filepath}.json не существует!" + RESET)
            if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: Базы данных {filepath}.json не существует\n")
                        else:
                            log.write(f"\n{log_time}: Базы данных {filepath}.json не существует")
            return
    
    def columns(self, filepath: str):
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
                        current_time = datetime.now()
                        name = current_time.strftime("%d.%m.%y")
                        log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                        with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                            if not log.read():
                                log.write(f"{log_time}: База данных {filepath}.json имеет: {int_count} интенджеров, {str_count} строк\n")
                            else:
                                log.write(f"\n{log_time}: База данных {filepath}.json имеет: {int_count} интенджеров, {str_count} строк")
            return int_count, str_count
        except:
            print("BarlaDB: " + RED + f"Базы данных {filepath}.json не существует!" + RESET)
            if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: Базы данных {filepath}.json не существует\n")
                        else:
                            log.write(f"\n{log_time}: Базы данных {filepath}.json не существует")
            return
    
    def restore_backup(self, BackupFilepath: str, DatabaseFilepath: str, RemoveBackupFile=True):
            if os.path.exists(BackupFilepath):
                pass
            else:
                print("BarlaDB: " + RED + f"Файла бэкапа не существует. ({BackupFilepath})" + RESET)
                if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: Файла бэкапа не существует. ({BackupFilepath})\n")
                        else:
                            log.write(f"\n{log_time}: Файла бэкапа не существует. {BackupFilepath}")
                return
            if os.path.exists(DatabaseFilepath):
                pass
            else:
                print("BarlaDB: " + RED + f"Файла базы данных не существует. ({DatabaseFilepath})" + RESET)
                if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: Файла базы данных не существует. ({DatabaseFilepath})\n")
                        else:
                            log.write(f"\n{log_time}: Файла базы данных не существует. ({DatabaseFilepath})")
                return
            with open(BackupFilepath, "r") as file:
                BackupData = json.load(file)
            with open(DatabaseFilepath, "w") as file:
                json.dump(BackupData, file, ensure_ascii=True, indent=2)
            print("BarlaDB: " + GREEN + "Успешный возврат до бэкапа!" + RESET)
            if config.log:
                current_time = datetime.now()
                name = current_time.strftime("%d.%m.%y")
                log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                    if not log.read():
                        log.write(f"{log_time}: Успешный возврат до бэкапа\n")
                    else:
                        log.write(f"\n{log_time}: Успешный возврат до бэкапа")
            if RemoveBackupFile:
                os.remove(BackupFilepath)
                if config.debug:
                    print("BarlaDB: " + GREEN + "Файл бэкапа успешно удалён!" + RESET)
                if config.log:
                    current_time = datetime.now()
                    name = current_time.strftime("%d.%m.%y")
                    log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
                    with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
                        if not log.read():
                            log.write(f"{log_time}: Файл бэкапа успешно удалён\n")
                        else:
                            log.write(f"\n{log_time}: Файл бэкапа успешно удалён")
