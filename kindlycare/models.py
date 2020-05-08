from kindlycare import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
'''
docs = db.Table('docs',
        db.Column('doc_id',db.Integer,db.ForeignKey('Doctors.id')),
        db.Column('hosp_id',db.Integer,db.ForeignKey('hospital.id'))
    )

services = db.Table('services',
        db.Column('service_id',db.Integer,db.ForeignKey('services.id')),
        db.Column('hosp_id',db.Integer,db.ForeignKey('hospital.id'))
    )'''
    '''
class Feedback(db.Model):
    __tablename__='feedback'
    id = db.Column(db.Integer,primary_key=True)
    hosp_id = db.Column(db.Integer,db.ForeignKey('hospital.id'))
    desc = db.Column(db.Text) 

class services(db.Model):
    __tablename__='services'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
'''    

class Hospitals(db.Model):
    __tablename__ = 'hospital'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    speciality = db.Column(db.String(50))
    description = db.Column(db.Text)
    contact_no = db. Column(db.Integer)
    address = db.Column(db.Text)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    days = db.Column(db.PickleType)
    #services = db.Column(db.ARRAY(String))
    #doctors = db.relationship('Doctors',secondary=docs,backref=db.backref('hospital',lazy = 'dynamic'))
    #feedbacks = db.relationship('feedback',backref='hospital')

