from flask import (
    Flask,
    jsonify,
    request,
)

from validator import validate

from db import (
    get_connection,
    get_shortest_distance,
)


app = Flask(__name__)


@app.route('/get_distance', methods=('POST', ))
def distance():
    if request.method == 'POST':

        posted_cities = request.get_json()
        validation_res = validate(posted_cities)
        if not validation_res['flag']:
            return jsonify(status=validation_res['message'])

        conn = get_connection()
        from_city = posted_cities['from_city']
        to_city = posted_cities['to_city']
        shortest_distance = get_shortest_distance(conn,
                                                  from_city=from_city,
                                                  to_city=to_city)

        return jsonify(distance=shortest_distance)


@app.route('/health', methods=('GET', ))
def health():
    status = '200. Application is running...'
    return jsonify(status=status)


if __name__ == '__main__':
    app.run(debug=False)
