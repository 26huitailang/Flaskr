from flask import Flask
from .movie.movie import movie


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(movie, url_prefix='/movie') # 这个url_prefix参数会影响浏览器访问和路由
    app.config.from_object('config')
    # app.config.from_pyfile('config.py')
    return app
