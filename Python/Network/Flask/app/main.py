from flask import Flask, request, make_response, redirect, abort
from flask import render_template
from jinja2 import Template
#import  views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
#import views

#if __name__ == '__main__':
#    print(app.url_map)
#    app.run(debug=True, host="localhost", port=5050)

