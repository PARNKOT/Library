from flask import Flask, request, make_response, redirect, abort
from flask import render_template
from jinja2 import Template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#if __name__ == '__main__':
#    print(app.url_map)
#    app.run(debug=True, host="localhost", port=5050)

