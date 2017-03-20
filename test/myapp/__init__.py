# coding: utf-8
import os
from flask import Flask
# from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from .main import main
from .ezbp import ezbp
from .vip import vip
from .movie import movie

db = SQLAlchemy()
# bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    basedir = os.path.abspath(os.path.dirname(__file__))
    # 声明ORM底层所用数据库的访问URL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
    # 当关闭数据库连接时是否自动提交事务
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    db.init_app(app)
    # bootstrap.init_app(app)

    app.register_blueprint(main, url_prefix='/main')
    app.register_blueprint(ezbp, url_prefix='/ezbp')
    app.register_blueprint(vip, url_prefix='/vip')
    app.register_blueprint(movie, url_prefix='/movie')
    return app

from . import models