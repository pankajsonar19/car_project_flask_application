
import datetime
import os


class Config(object):



    #jwt
   # JWT_AUTH_URL_RULE = '/api/login'
    #JWT_EXPIRATION_DELTA = datetime.timedelta(days=31)

    #SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

# for development and testing env
class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'sqlite://///home/ubuntu/sqlite/car.db'


# for production env
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False



# dictionary to decide env
config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)