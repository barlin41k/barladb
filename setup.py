from setuptools import setup

setup(
    name='barladb',
    version='0.2.0',
    description='A very easy local database based on JSON',
    packages=['barladb'],
    author_email='sasaigrypocta@gmail.com',
    author="barlin41k",
    zip_safe=False,
    long_description='''
# Изменения:
- Структура `db.py` была изменена на класс с функцией `__init__`
- Удалена зависимость: `colorama`


# Что такое barlaDB?
- `barlaDB` - это легкая, простая библиотека для небольших проектов на `Python`, которая имеет очень лёгкий интерфейс. С ней смогут познакомиться даже чайники в `Python`!

# Лёгкий пример использования
```python
from barladb import db #Импортирование функций БД
from barladb import config #Импортируем конфиг для того чтобы подключить логирование действий
config.debug = True #Включение логирования

db = db.BarlaDB() #Создание экземпляра класса
data = db.get("example") #Достаем содержимое БД и сохраняем его в переменную data. Заметьте, что мы не пишем расширение (.json)
#Также, если ваш файл находится в другой папке, всего-лишь требуется прописать другой путь, к примеру
#db.get("path/to/file/example")

name = data["name"] #Достаём столбец name из example.json
age = data["age"] #Тоже самое только столбец age
print(f"Привет, {name}! Тебе {age} лет, верно?!")
if age > 60:
    print("Стоп, тебе не может быть больше 60 лет...")
else:
    raise SystemExit(1)

print("Сейчас мы поменяем тебе возраст на 18 лет...")
data["age"] = 18 #Теперь столбец age равен 18
db.save("example", data) #Сохранения данных в example.json
```
# Как установить?
- `pip install barladb`

# Особенности barlaDB
- Простота в использовании
- Очень лёгкий интерфейс
- Базирована на всеми известном `JSON`
    ''',
    long_description_content_type="text/markdown",
    url="https://github.com/barlin41k/barladb",
    project_urls={
        "Documentation": "https://sites.google.com/view/barladb/",
        "GitHub": "https://github.com/barlin41k/barladb",
    })
