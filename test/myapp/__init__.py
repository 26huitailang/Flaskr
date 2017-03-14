# coding: utf-8
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

basedir = os.path.abspath(os.path.dirname(__file__))
# 声明ORM底层所用数据库的访问URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
# 当关闭数据库连接时是否自动提交事务
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

from . import views, models