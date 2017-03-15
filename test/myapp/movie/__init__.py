from flask import Blueprint

movie = Blueprint('movie', __name__,
                  template_folder='templates',
                  static_folder='static')

from . import views