import werkzeug

from app.models.models import Car_db, carschema
from app.database import db

from flask_restplus import Namespace, Resource, fields, abort, reqparse
from flask import request
import pandas as pd

from sqlalchemy.sql import func
from sqlalchemy import or_, and_
from sqlalchemy.orm import load_only
from app.common import (logging,token_required)


ns_cars = Namespace('cars',
                    description='namespace for the cars data')

# restplus model for marshalling with the database records
car_model = ns_cars.model('Cars', {

    'chassis_no': fields.String(
        required=True,
        example='12345A'
    ),

    'make': fields.String(
        required=True,
        example='Nissan'
    ),
    'model': fields.String(
        required=True,
        example='Micra'
    ),

    'year': fields.Integer(
        required=True,
        example='2004'
    ),
    'id': fields.Integer(
        required=True,
        example='101'
    ),
    'last_updated': fields.DateTime(
        required=True,
        example='2018-02-09 10:11:11'
    ),
    'price': fields.Float(
        required=True,
        example='500.0'
    )
})

# restplus model for considering 'model' and 'make' for finding average price
price_model = ns_cars.model('Average_Price', {

    'make': fields.String(
        required=True,
        example='Nissan'
    ),
    'model': fields.String(
        required=True,
        example='Micra'
    )
})

parser = reqparse.RequestParser()
parser.add_argument('car_data', type=werkzeug.datastructures.FileStorage, location='files', required=True)
parser1 = reqparse.RequestParser()
parser1.add_argument('Authorization', type = str, location='headers',help='Bearer Firebase Access Token',required=True)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


@ns_cars.route('/read_file')
class Read_file(Resource):
    @ns_cars.expect(parser)
    def post(self):
        try:
            csv_file = request.files['car_data']

            df = pd.read_csv(csv_file)
            logging.info('The data is : %r', df)

            engine = db.get_engine()

            df.to_sql(name=Car_db.__tablename__, con=engine, if_exists='replace', index=False,
                      index_label='chassis_no')  # if_exists="fail,append,replace" you can keep anything as per requirement

            return 'File read successfully', 201


        except Exception as e:
            db.session.rollback()
            abort(400, e.args[0])
        finally:
            db.session.close()


@ns_cars.route('/<int:id>')
class Car_ID(Resource):
    @ns_cars.expect(parser1) # only authenticated user can be able to retreive the data from database
    def get(self, id):
        try:
            token = request.headers.get('Authorization').replace("Bearer ", "").strip()

            car = Car_db.query.with_entities(Car_db.id, Car_db.make, Car_db.model, Car_db.year, Car_db.last_updated,
                                             Car_db.price).filter(Car_db.id == id).all()

            car = carschema.dump(car, many=True).data

            logging.info('Response json: %r', car)

            return car, 200
        except Exception as e:
            db.session.rollback()
            abort(400, e.args[0])
        finally:
            db.session.close()


@ns_cars.route('/avg_price')
class Car_Avg_Price(Resource):
    @ns_cars.expect(price_model)
    def post(self):

        try:

            data = request.get_json()

            make = data['make']
            model = data['model']

            # considering combinations of make and model for returning the average price
            ans = Car_db.query.with_entities(Car_db.make, func.avg(Car_db.price).label('average_price')).filter(
                and_(Car_db.make == make, Car_db.model == model)).group_by(Car_db.make).all()
            if ans == []:
                logging.info('Record not found. Please enter valid combination of make and model')
                return {'message': 'Record not found. Please enter valid combination of make and model'}
            else:
                logging.info('Average price: %r', ans)
                return ans

        except Exception as e:
            db.session.rollback()
            abort(400, e.args[0])
        finally:
            db.session.close()
