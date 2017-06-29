"""
"""
from flask import render_template

from . import code


@code.route('/socketchat')
def socket_chat():
    return render_template('socket_chat.html', title='Socket Chat')


@code.route('/atmo')
def atmo():
    render_template('atmo.html', title='atmo')