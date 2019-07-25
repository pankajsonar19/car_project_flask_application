from app.database import db
from sqlalchemy import (Integer, Column, ForeignKey, Boolean, String, Date, DateTime,Float)
from marshmallow_sqlalchemy import ModelSchema, ModelConverter





class Car_db(db.Model):
    __tablename__ = 'car_info'
    make = db.Column('make',String(80))
    model = db.Column('model',String(80))
    year = db.Column('year',Integer)
    chassis_no = db.Column('chassis_no',String(80), primary_key=True)
    id = db.Column('id',Integer)
    last_updated = db.Column('last_updated',DateTime)
    price = db.Column('price',Float)

class Car_Schema(ModelSchema):
    class Meta:
        model = Car_db

carschema = Car_Schema()