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

class Feedback(db.Model):
    __tablename__='feedback'
    id = db.Column(db.Integer,primary_key=True)
    hosp_id = db.Column(db.Integer,db.ForeignKey('hospital.id'))
    desc = db.Column(db.Text) 
'''
class services(db.Model):
    __tablename__='services'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
'''    

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(), unique=True)
    password_hash = db.Column(db.String(128))
    profile_image = db.Column(
        db.String(20), nullable=False, default='default_profile.png')

    def __init__(self, name, email, password):
        self.email = email
        self.name = name
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'{self.name}{self.email}'
