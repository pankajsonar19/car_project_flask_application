import logging

from flask import (Flask, redirect, session)

from werkzeug.contrib.fixers import ProxyFix
from .config import config_by_name, DevelopmentConfig

from app.rest_api.car_api import blueprints
from app.models.models import Car_db




from app.database import db
from flask_migrate import Migrate



def create_app(config_name):
    """ factory pattern to instantiate app for given environment """
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    config_name = config_name or 'dev'
    app.config.from_object(config_by_name[config_name])

    '''
    @app.errorhandler(Exception)
    def all_exception_handler(error):
        logging.exception(error)
        return 'An Error occurred', 400

    @app.before_request
    def check_auth():
        """ enforce JWT authentication for all non-whitelisted paths """
        path = request.path
        logging.info('path %r', path)
        if 'username' in session or not path.startswith('/api/'):
            return None

        allowed_paths = ['/api/forgot_password',
                         '/api/',
                         '/api/register',
                         '/api/resend',
                         '/api/clients',
                         '/api/login']
        pattern_allowed_paths = '|'.join(
            re.escape(p) for p in allowed_paths)

        # these paths are allowed without JWT token
        if (re.match(r'^(?:%s)$'
                     % (pattern_allowed_paths,), path) or path == '/'):
            return None
        if path.startswith('/api/confirm'):
            return None

        realm = app.config['JWT_DEFAULT_REALM']
        return _jwt_required(realm)

    jwt.init_app(app)
    '''
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app,db)


    app.app_context().push()

    # register the car_api blueprints
    app.register_blueprint(blueprints, url_prefix='/api/v1')

    return app
