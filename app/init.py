
from app.database import db

def init():
    db.create_all()