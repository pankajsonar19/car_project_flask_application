import logging

from pythonjsonlogger import jsonlogger

from functools import wraps

from flask import request


# Define a logging mechanism for your application
logger = logging.getLogger()

logger.setLevel(logging.INFO)

logHandler = logging.FileHandler('test.log')

format =' (levelname) (asctime) (funcName) (message)'

formatter = jsonlogger.JsonFormatter(format)

logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

def token_required(tk):
    @wraps(tk)
    def decorated(*args, **kwargs):
        token = None
        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']
        if not token:
            return {'message': 'token is missing'}

        return tk(*args, **kwargs)

    return decorated()