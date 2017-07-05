"""
"""
from flask import render_template

from admrsh import api
from . import code
from .models import AtmoReadings


@code.route('/socketchat')
def socket_chat():
    return render_template('socket_chat.html', title='Socket Chat')


@code.route('/atmo')
def atmo():
    return render_template('atmo.html', title='atmo')


api.add_resource(AtmoReadings, '/atmo_api')