# all the configurations, env variables, secret keys etc to be declared here.
# may change for different environments like Development, Testing, Staging and Production

import os


class Config(object):
    # SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True


# for development env
class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///car.db'


# for testing env
class TestingConfig(Config):
    DEBUG = True
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///car_test.db'


# for staging env
class StagingConfig(Config):
    DEBUG = True
    TESTING = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///car_staging.db'


# for production env
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

    # all the information related to production env
    SQLALCHEMY_DATABASE_URI = 'sqlite:///car.db'


# dictionary to decide env
config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
