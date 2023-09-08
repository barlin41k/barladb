from barladb import db #Импортирование функций БД
from barladb import config #Импортируем конфиг
config.debug = True #Включение дебага
config.log = True #Включение лога

barladb = db.BarlaDB() #Создание экземпляра класса
data = barladb.get("example") #Достаем содержимое БД и сохраняем его в переменную data
#Также, если ваш файл находится в другой директории:
#db.get("path/to/file/example")

name = data["name"]
age = data["age"]
print(f"Привет, {name}! Тебе {age} лет, верно?!")
if age > 60:
    print("Стоп, тебе не может быть больше 60 лет...")
else:
    exit(-1)

print("Сейчас мы поменяем тебе возраст на 18 лет...")
data["age"] = 18
barladb.save("example", data) #Сохранения данных в example.json
