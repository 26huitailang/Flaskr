# coding: utf-8
from . import vip
from flask import render_template


@vip.route('/')
def index():
    return render_template('page.html')
