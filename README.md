# Изменения:
- Приятный для глаз интерфейс файлов
- Незначительные изменения
- Исправления багов

# ToDo
- Переделать интерфейс на английскую версию


# Что такое barlaDB?
- `BarlaDB` - библиотека, которая создана для работ с локальными базами данных в формате `.json`. Имеет хорошо проработанные функции и логирование! А самое главное - имеет очень лёгкий для изучения интерфейс, даже новичку!

# Лёгкий пример использования
```python
from barladb import db #Импортирование функций БД
from barladb import config #Импортируем конфиг
config.debug = True #Включение дебага
config.log = True #Включение лога

barladb = db.BarlaDB() #Создание экземпляра класса
data = barladb.get("example") #Достаем содержимое БД и сохраняем его в переменную data. Заметьте, что мы не пишем расширение (.json)
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
```
# Как установить?
- `pip install barladb`

# Особенности barlaDB
- Имеет лёгкий и понятный интерфейс
- Не имеет зависимостей
- Всё построено на популярном `.json` формате данных

# Ссылки
- [Documentation](https://sites.google.com/view/barladb/)
- [Github](https://github.com/barlin41k/barladb/)
- [PyPi](https://pypi.org/project/barladb/)
