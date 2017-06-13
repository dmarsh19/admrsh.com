"""
"""
from flask import render_template

from . import base


@base.route('/')
def home():
    return render_template('home.html', title='Home')


@base.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
