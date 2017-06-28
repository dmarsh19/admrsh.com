"""
"""
from flask import render_template

from . import code


@code.route('/infrastructure')
def infrastructure():
    return render_template('infrastructure.html', title='Infrastructure')


@code.route('/socketchat')
def socket_chat():
    return render_template('socket_chat.html', title='Socket Chat')
