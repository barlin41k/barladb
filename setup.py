from setuptools import setup

setup(
    name='barladb',
    version='0.1.7',
    description='A very easy local database based on JSON',
    packages=['barladb'],
    author_email='sasaigrypocta@gmail.com',
    author="barlin41k",
    zip_safe=False,
    long_description='''
# Изменения:
- Добавлены новые функции и документация - https://sites.google.com/view/barladb/
```python
db.remove_column(filepath, key)
db.columns(filepath)
```


# Что такое barlaDB?
- `barlaDB` - это легкая, простая библиотека для небольших проектов на `Python`, которая имеет очень лёгкий интерфейс. С ней смогут познакомиться даже чайники в `Python`!

# Лёгкий пример использования
```python
from barladb import db #Импортирование функций БД
from barladb import config #Импортируем конфиг для того чтобы подключить логирование действий
config.debug = True #Включение логирования

#В этом примере уже создан файл БД (example.json)
#И если вам понадобится в каких то функциях создавать БД с названием, воспользуйтесь
#db.create(название_БД)
data = db.get("example") #Достаем содержимое БД и сохраняем его в переменную data. Заметьте, что мы не пишем расширение (.json)
#Также, если ваш файл находится в другой папке, всего-лишь требуется прописать другой путь, к примеру
#db.get("path/to/file/example")
#Надеюсь, что этот вариант тоже будет работать
name = data["name"] #Достаём столбец name из example.json (Буду называть дальше это как "БД")
age = data["age"] #Тоже самое только столбец age
print(f"Привет, {name}! Тебе {age} лет, верно?!")
if age > 60:
    print("Стоп, тебе не может быть >60 лет...")
else:
    raise SystemExit(1) #Выходим из выполнения кода
#Поскольку мы сделали выход если <60 лет указано в нашем БД, то остались в программе только >60 лет (По БД, еще раз повторяю)
print("Сейчас мы поменяем тебе возраст на 18 лет...")
data["age"] = 18 #Теперь столбец возраста равен 18 лет
db.save("example", data) #Сохранения данных в БД
#А дальше уже была другая история...
#Можно было с помощью db.delete(название_БД) удалить теперь БД, но для этого будет документация, этого всего лишь пример кода))
```
# Как установить?
- `pip install barladb`

# Особенности barlaDB
- Простота в использовании
- Очень лёгкий интерфейс
- Базирована на всеми известном `JSON`
    ''',
    long_description_content_type="text/markdown",
    url="https://sites.google.com/view/barladb/",
    project_urls={
        "Documentation": "https://sites.google.com/view/barladb/",
    })