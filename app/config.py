
import datetime
import os


class Config(object):



    #jwt
   # JWT_AUTH_URL_RULE = '/api/login'
    #JWT_EXPIRATION_DELTA = datetime.timedelta(days=31)

    #SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

# for development env
class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite://///home/ubuntu/sqlite/car.db'

# for testing env
class TestingConfig(Config):
    DEBUG = True
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'sqlite://///home/ubuntu/sqlite/car_test.db'

# for staging env
class StagingConfig(Config):
    DEBUG = True
    TESTING = False

    SQLALCHEMY_DATABASE_URI = 'sqlite://///home/ubuntu/sqlite/car_staging.db'

# for production env
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

    # all the information related to production env


# dictionary to decide env
config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)