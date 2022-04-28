from flask import (
    Flask,
    redirect,
    request,
    render_template,
)


app = Flask(__name__)


@app.route('/city', methods=('GET', 'POST'))
def city():
    if request.method == 'POST':
        from_city = request.form['from_city']
        to_city = request.form['to_city']

        distance = from_city + to_city
        location = f'http://127.0.0.1:5000/get_distance/{distance}'

        return redirect(location)

    return render_template('form_city.html')


@app.route('/get_distance/<distance>')
def distance(distance):

    ctx = {'res': distance}
    return render_template('distance.html', **ctx)


if __name__ == '__main__':
    app.run(debug=True)
