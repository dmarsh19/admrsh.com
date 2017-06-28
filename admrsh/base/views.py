"""
"""
from flask import render_template

from . import base


@base.route('/')
def home():
    return render_template('home.html', title='Home')
