# coding: utf-8
from . import db

class User(db.Model):
    # __tablename__ = 'ezuser'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    age = db.Column(db.Integer)
    tel = db.Column(db.String(20))

    def __init__(self, id, name, age, tel):
        self.id = id
        self.name = name
        self.age = age
        self.tel = tel


class Log(User):
    # __tablename__ = 'log'  # 默认使用类名作为表名
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    desc = db.Column(db.String(1024))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))