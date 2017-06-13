"""
"""
import os
import logging

from flask import Flask


# create the application object
app = Flask(__name__)
# pulls in app configuration from settings.py
app.config.from_object('settings')

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
from .base import base
from .projects import projects
from .code import code

# register the individual blueprints (modules) to the app
app.register_blueprint(base)
app.register_blueprint(projects, url_prefix='/projects')
app.register_blueprint(code, url_prefix='/code')
