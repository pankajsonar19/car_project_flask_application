# a init file to run DDL commands i.e table creation for test cases (pytest)

from app.database import db

def init():
    db.create_all()