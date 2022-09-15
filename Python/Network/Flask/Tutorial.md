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
1) from flask import make_response, redirect, abort
2) Ответы могут быть трех типов:
    - В виде строки: return "string"
    - Объект ответа: return make_response("body", status_code, headers)
    - Кортеж:        return ("string", status_code, headers) //type(headers) = dict
3) response = make_response("string", 200)
    - response.headers["header"] = value
    - response.set_cookie("string", "string", keep_alive)
    - return response
4) return redirect("address")
5) @app.before_request()
    - def before_request():
6) @app.after_request()
    - def after_request(response): ... return response