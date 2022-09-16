# Работа со статическими файлами
> 1. `app = Flask(__name__, static_folder="static_dir")`  
По умолчанию `static_folder="static"`

> 2. `<script src="{{ url_for('static', filename='jquery.js') }}"></script>`
