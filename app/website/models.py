from . import db 
from flask_login import UserMixin
#from sqlalchemy.sql import func
#
#
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, func,create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime
from sqlalchemy_utils import database_exists
from test_postgre import engine, Session


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #func_now() = current date and time 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # No user can have the same email than another user
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') 



#Base = declarative_base()
#locale_session = Session(bind=engine)
##Base.query = locale_session.query_property()
#
#class Note(Base):
#    __tablename__= 'Note'
#    id = Column(Integer, primary_key=True)
#    data = Column(String(10000))
#    date = Column(DateTime(timezone=True), default=func.now()) #func_now() = current date and time 
#    user_id = Column(Integer,ForeignKey('Users.id'))
#
#class User(Base):
#    __tablename__= 'Users'
#    id = Column(Integer, primary_key=True)
#    email = Column(String(150), unique=True) # No user can have the same email than another user
#    password = Column(String(150))
#    first_name =Column(String(150))
#    notes = relationship('Note') 
