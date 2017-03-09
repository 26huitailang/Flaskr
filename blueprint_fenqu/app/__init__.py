from flask import Flask
from .movie.movie import movie


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(movie)
    app.config.from_object('config')
    # app.config.from_pyfile('config.py')
    return app
