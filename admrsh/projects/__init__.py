"""
"""
from flask import Blueprint

projects = Blueprint('projects',
                     __name__,
                     template_folder='templates')#,
                     #static_folder='static',
                     #static_url_path='/static/base')

from . import views
