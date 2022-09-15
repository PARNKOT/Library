from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
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


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
