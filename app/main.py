# this is my application manage/main.py file which contains create_app() function and all the initialization
# of the different apps is done here

import logging

from flask import (Flask, redirect, session, request)

# from werkzeug.contrib.fixers import ProxyFix
from werkzeug.middleware.proxy_fix import ProxyFix
from .config import config_by_name, DevelopmentConfig

from app.rest_api.car_api import blueprints
from app.models.models import Car_db

from app.database import db
from flask_migrate import Migrate


def create_app(config_name=None):

    """ factory pattern to instantiate app for given environment """
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # to decide which configuration app is running of (Development, Testing or Production)
    config_name = config_name  # or 'dev'
    app.config.from_object(config_by_name[config_name])

    # Initialization of flask-sqlalchemy, flask-migrate
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)

    # register the car_api blueprints
    app.register_blueprint(blueprints, url_prefix='/api/v1')

    # to keep track of application level context
    app.app_context().push()

    return app
