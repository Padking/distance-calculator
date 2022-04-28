import json

import requests


cities = {
    'from_city': 5,
    'to_city': 1,
}
cities_ = json.dumps(cities)
headers = {
    'Content-Type': 'application/json',
}


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/get_distance'
    r = requests.post(url, data=cities_, headers=headers)
    print(r.json())
