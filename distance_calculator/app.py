from flask import (
    Flask,
    redirect,
    request,
    render_template,
)

from .graph import get_distance


app = Flask(__name__)


@app.route('/city', methods=('GET', 'POST'))
def city():
    if request.method == 'POST':
        from_city = int(request.form['from_city'])
        to_city = int(request.form['to_city'])

        distance = get_distance(from_city, to_city)
        location = f'http://127.0.0.1:5000/get_distance/{distance}'

        return redirect(location)

    return render_template('form_city.html')


@app.route('/get_distance/<distance>')
def distance(distance):

    ctx = {
        'res': distance,
        'dimension': 'км.'
    }

    return render_template('distance.html', **ctx)


if __name__ == '__main__':
    app.run(debug=True)
