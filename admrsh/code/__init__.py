"""
"""
from flask import Blueprint

code = Blueprint('code', __name__,
                 template_folder='templates')

from . import views
