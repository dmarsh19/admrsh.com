"""
"""
from flask import render_template

from . import code


@code.route('/infrastructure')
def infrastructure():
    return render_template('infrastructure.html', title='Infrastructure')
