"""
"""
from flask import render_template

from . import base


@base.route('/')
def home():
    return render_template('home.html', title='Home')

@base.route('/code')
def code():
    return render_template('code.html', title='Code Samples')

@base.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')

@base.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
