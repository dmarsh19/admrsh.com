import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

# create the application object
app = Flask(__name__)
# pulls in app configuration from settings.py
app.config.from_object('settings')

db = SQLAlchemy(app)
# flask_restful api resources
# add the api blueprint to the api object within api/__init__.py
api = Api()

#TODO: write to /var/log
# will cause permission issues if its within a users home directory
# # create logger
# logging.basicConfig(filename=app.config['APP_LOGFILE'],
#                     filemode='a+',
#                     level=logging.DEBUG,
#                     format='%(asctime)s %(name)s %(levelname)s %(message)s')
# LOG = logging.getLogger(__name__)
# if not app.config['DEBUG']:
#     logging.disable(10)


# import modules (have to import at the end after all app configurations are instantiated)
from .base import base_bp
from .code import code_bp
from .api import api_bp

# register the individual blueprints (modules) to the app
app.register_blueprint(base_bp)
app.register_blueprint(code_bp, url_prefix='/code')
app.register_blueprint(api_bp, url_prefix='/api')
