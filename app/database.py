# Declaring the flask-sqlalchemy. Keeping it seperate so that in later stage if we have any circular dependent models then
# it should not create any issue.

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()