from flask import Flask, request, make_response, redirect, abort
from flask import render_template
from jinja2 import Template


app = Flask(__name__)


@app.route('/index1')
def index1():
    return "Hello, world!"


@app.route('/pages/<page>')
def pages(page: int):
    return f"Page: {page}"


@app.route('/paths/<path:path>')
def paths(path):
    return f"{path}"


@app.route('/address')
def address():
    return f'address: {request.remote_addr}, user: {request.remote_user}'


@app.route('/make_response')
def make_response_test():
    response = make_response('Make response', 200)
    response.headers['Content-type'] = 'text/plain'
    response.headers['Server'] = 'Egor'
    response.set_cookie("favorite-color", "skyblue", 100)
    response.set_cookie("favorite-font", "sans-serif", 100)
    return response


@app.route('/tuple_response')
def tuple_response():
    return (
        'tuple_response',
        200,
        {
            'flask': 222,
        }
    )


@app.route('/transfer')
def transfer():
    return redirect('http://localhost:5000/pages/123') # or ('', 302, {'location': 'http://localhost:5000/pages/123'})

# Перехват запросов
@app.before_request
def before_request():
    print('before_request')


@app.after_request
def after_request(response):
    print('after_request')
    return response

@app.route('/abort')
def abort_test():
    print('abort')
    abort(500)


@app.errorhandler(404)
def error404handler(error):
    return "<h1>OMG, it is 404!</h1>"


@app.route('/')
def index():
    # t = Template('templates/index.html')
    return render_template('index.html', name='Egor')


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)

