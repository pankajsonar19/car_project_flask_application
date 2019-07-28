# this file contains some common stuffs that can be used in whole application
# I am writing the log definitions here

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

