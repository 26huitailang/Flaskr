from flask import Blueprint, render_template, current_app, request
from pymongo import MongoClient

movie = Blueprint('movie', __name__,
                  template_folder='templates',
                  static_folder='static')


def connect_db():
    client = MongoClient()
    db = client['dytt']
    col = db['zuixindianying']
    return col


# TODO all without buxiangkan
@movie.route('/', methods=['GET'])
def show_items():
    col = connect_db()
    items = col.find({})
    print(request.cookies)
    return render_template('show_items.html', items=items)


# TODO buxiangkan

# TODO yikan
