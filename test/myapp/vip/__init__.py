from flask import Blueprint

vip = Blueprint("vip", __name__, static_folder="assets", template_folder="templates")

from . import views