from sqlalchemy.sql import func
from app.extensions import db

import datetime
from passlib.hash import sha256_crypt
import sys

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.VARCHAR(100), nullable=False, unique=True)
  password = db.Column(db.VARCHAR(200), nullable=False)
  email = db.Column(db.VARCHAR(200), nullable=False)
  permission = db.Column(db.Integer, server_default= "0")
  last_login = db.Column(db.DateTime(timezone=True),
                          server_default=func.now())
