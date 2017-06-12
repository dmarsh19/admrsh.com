"""
"""
from flask import render_template

from . import projects


@projects.route('/socketchat')
def socketchat():
    return render_template('projects.html', title='Socket Chat')
