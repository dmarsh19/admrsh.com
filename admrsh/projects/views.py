"""
"""
from flask import render_template

from . import projects


@projects.route('/socketchat')
def socket_chat():
    return render_template('socket_chat.html', title='Socket Chat')
