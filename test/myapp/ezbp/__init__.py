from flask import Blueprint

ezbp = Blueprint("ezbp", __name__)

from . import views