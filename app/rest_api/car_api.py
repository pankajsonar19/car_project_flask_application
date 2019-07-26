# write here the api routings

from flask import Blueprint
from flask_restplus import Api, Resource
from jsonschema import FormatChecker

from app.views.v1.cars import ns_cars

#from app.views.v1.cars import authorizations


blueprints = Blueprint('api', __name__)
api = Api(blueprints,
          version='0.1',
          title='Car API',
          description='A Car Api to show its details',
          validate=True,
          format_checker=FormatChecker(formats=("date",)), )

# Bring in the rest of our API code here i.e to add namespaces


ns1 = api.add_namespace(ns_cars)
