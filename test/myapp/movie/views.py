from flask import Blueprint, render_template, current_app, request
from pymongo import MongoClient
from . import movie


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
    return render_template('movie/show_items.html', items=items)

@movie.route('/index')
def index():
    return render_template('movie/index.html')

@movie.route('/carousel')
def carousel():
    return render_template('movie/carousel.html')

@movie.route('/tabs')
def tabs():
    return render_template('movie/tabs.html')

@movie.route('/books')
def books():
    return render_template('movie/books.html')
# TODO buxiangkan

# TODO yikan
