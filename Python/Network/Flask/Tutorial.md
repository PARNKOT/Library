# Основы
1) from flask import Flask
2) Создание экземпляра приложения:
    - app = Flask(__name__)
    // __name__ используется flask'ом для поиска файлов
3) Запуск приложения:
    - app.run()
    - app.run(debug=True)
4) Маршрутизация:
    - @app.route("/")
    - @app.route("/<converter:var>")
      def index(var):
        ...
    // converter: int, string, float, path, uuid
    // var: имя переменной
    // app.url_map: список маршрутов

# Контексты
1) from flask import request, current_app
2) Когда появляется запрос, то активируется контекст запроса.
   Возможно использование объекта request
   - request.remote_addr
   - request.remote_user
   - ...
3) Также существует контекст приложения
   Доступ через объект current_app

# Ответ сервера и перехват запросов
1) 