from flask import Blueprint

from admrsh import api

api_bp = Blueprint('api', __name__)
api.init_app(api_bp)

from . import resources
