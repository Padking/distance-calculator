# Distance Calculator

Web API сервис кратчайших путей

## Описание

Сервис расчитывает кратчайшее расстояние между 2-мя локациями

### Начало работы

- Необходимо:
  + [наполнить](https://github.com/Padking/distance-calculator#установка) базу данных (БД).


### Особенности

- ограничения:
  + матрица смежности [бинарного файла](https://github.com/Padking/distance-calculator/blob/master/data/matrix_distance) размерностью 50х50
  + диапазон порядковых номеров локаций для POST-запроса - от 0 до 49 включительно
- источник данных: [бинарный файл](https://github.com/Padking/distance-calculator/blob/master/data/matrix_distance),
- статус проекта: учебный.

### Пример исходных данных

- дешифрированное содержимое [бинарного файла](https://github.com/Padking/distance-calculator/blob/master/data/matrix_distance):
```sh
[0 7 8 5 2 7 4 5 3 0 7 1 0 6 9 8 0 0 5 1 3 4 6 1 4 6 0 8 3 2 3 5 7 4 7 3 7
 5 5 6 2 4 8 0 2 5 1 4 0 0]
[7 0 5 7 8 1 5 2 7 2 8 2 4 8 3 6 1 2 4 4 6 7 8 5 8 2 7 5 3 5 4 4 2 3 5 4 9
 4 9 4 9 3 2 7 1 8 6 2 2 7]
```

- формат POST-запроса:
```python
cities = {
    'from_city': 15,
    'to_city': 1,
}
```

### Используемые технологии

* [Flask](https://flask.palletsprojects.com/en/latest/)
* [Numpy](https://numpy.org/doc/stable/reference/index.html)
* [Pandas](https://pandas.pydata.org/docs/index.html)
* [requests](https://requests.readthedocs.io/en/master/)

## Структура проекта

2 эндпоинта: [кратчайшего расстояния](https://github.com/Padking/distance-calculator/blob/master/distance_calculator/app.py#L18) и [оценки "здоровья" сервиса](https://github.com/Padking/distance-calculator/blob/master/distance_calculator/app.py#L35)

## Требования к окружению

* Python 3.7 и выше,
* Linux/Windows.

## Установка

- Клонировать проект:
```sh
git clone https://github.com/Padking/distance-calculator.git
cd distance-calculator
```
- Создать каталог виртуального окружения (ВО)*,
   связать каталоги ВО и проекта,
   установить зависимости:
```sh
mkvirtualenv -p <path to python> <name of virtualenv>
setvirtualenvproject <path to virtualenv> <path to project>
pip install -r requirements.txt
```

- установить переменные окружения для Flask-проекта

- наполнить БД информацией о кратчайших расстояниях между локациями:
```sh
cd distance_calculator/
python db.py
```
- запустить сервис,
- в новом окне терминала выполнить запрос от клиента (К),
- убедиться в наличии ответа.
```bash
python app.py
python client.py
```





\* с использованием [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)


### Пример запуска

- старт Flask-проекта:
```sh
$ python app.py
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

```

- корректный ответ:
```sh
$ python client.py
{'distance': 2}
```

- некорректный ответ:
```sh
$ python client.py
{'status': '400. Invalid input data'}
```


### Тестирование

[Примеры тестовых сценариев](https://github.com/Padking/distance-calculator/blob/master/client.py#L11)
