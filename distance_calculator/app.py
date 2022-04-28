from flask import (
    Flask,
    jsonify,
    request,
)

from .validator import validate

from .graph import get_distance


app = Flask(__name__)


@app.route('/get_distance', methods=('POST', ))
def distance():
    if request.method == 'POST':
        posted_cities = request.get_json()
        from_city = posted_cities['from_city']
        to_city = posted_cities['to_city']

        validate(from_city, to_city)

        distance = get_distance(from_city, to_city)

        return jsonify(distance=distance)


if __name__ == '__main__':
    app.run(debug=True)
