from flask import render_template

from . import base_bp


@base_bp.route('/')
def home():
    return render_template('home.html', title='Home')
