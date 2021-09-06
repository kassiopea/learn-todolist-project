from flask import Flask
from flask_cors import CORS

from todo_list_api.auth.helper import get_refresh_token
from todo_list_api.extentions import mongo, jwt, redis


def create_app(config_object='todo_list_api.settings'):
    app = Flask(__name__)

    app.config.from_object(config_object)

    mongo.init_app(app)
    redis.__init__(host='redis', decode_responses=True)
    jwt.init_app(app)

    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}},
         supports_credentials=True)

    from todo_list_api.users.routers import users
    from todo_list_api.auth import routers
    from todo_list_api.colors.routers import colors
    from todo_list_api.todo.routers import todo

    # app.register_blueprint(todo, url_prefix='/api/v1/todo_list/')
    # app.register_blueprint(colors, url_prefix='/api/v1/colors/')
    app.register_blueprint(users, url_prefix='/api/v1/users/')
    app.register_blueprint(routers.auth, url_prefix='/api/v1/auth/')

    # временно для проверки (потом удалить)
    @app.route('/')
    def index():
        return 'Hello from Docker!'

    @app.after_request
    def refresh_expiring_jwts(response):
        return get_refresh_token(response)

    return app
