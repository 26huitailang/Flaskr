# coding: utf-8
from flask import Flask, render_template, render_template_string
from config import contacts
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

basedir = os.path.abspath(os.path.dirname(__file__))
# 声明ORM底层所用数据库的访问URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# 当关闭数据库连接时是否自动提交事务
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

user = {'id': 123, 'nickname': '< IAMKING>'}
tpl1 = '<h1>homepage of <a href="/user/{{id}}">{{nickname | e}}</a></h1>'
# 递归循环
tpl2 = '''
    <ul>
        {% for item in friend_circle recursive %}
        <li>
            {{ item }}
            <ul>{{ loop(item.friends) }}</ul>
        </li>
        {% endfor %}
    </ul>
    '''
tpl3 = '''
    <ul>
        {% for item in contacts %}
        {% if loop.index % 2 == 0 %}
        <li class="even-row">{{ item }}</li>
        {% else %}
        <li class="odd-row">{{ item }}</li>
        {% endif %}
        {% endfor %}
    </ul>
    '''


@app.route('/string')
def v_index():
    return render_template_string(tpl3, contacts=contacts)


@app.route('/')
def index():
    return render_template('table.html', contacts=contacts)


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
