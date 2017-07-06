from flask import render_template

from . import code_bp


@code_bp.route('/socketchat')
def socket_chat():
    return render_template('socket_chat.html', title='Socket Chat')


@code_bp.route('/atmo')
def atmo():
    return render_template('atmo.html', title='atmo')
