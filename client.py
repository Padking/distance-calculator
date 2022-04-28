import json

import requests


cities = {
    'from_city': 15,
    'to_city': 1,
}

# Начало тестовых сценариев
cities_1 = {
    'from_city': 5,
}
cities_2 = {
    'to_city': 1,
}
cities_3 = {
    'from_cityAAA': 5,
    'to_city': 1,
}
cities_4 = {
    'from_city': 55,
    'to_city': 1,
}
# Конец тестовых сценариев

cities_ = json.dumps(cities)
headers = {
    'Content-Type': 'application/json',
}


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/get_distance'
    r = requests.post(url, data=cities_, headers=headers)
    print(r.json())
    # print(r.text)

    url = 'http://127.0.0.1:5000/health'
    r = requests.get(url)
    # print(r.json())
