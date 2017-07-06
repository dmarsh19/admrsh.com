from flask import Blueprint

code_bp = Blueprint('code', __name__,
                    template_folder='templates')

from . import views
