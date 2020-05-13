from kindlycare import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

relate = db.Table('relate',
        db.Column('doctor_id', db.Integer, db.ForeignKey('doctors.id')),
        db.Column('hospital_id', db.Integer, db.ForeignKey('hospital.id')))

'''

class services(db.Model):
    __tablename__='services'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
'''    

class Hospitals(db.Model):
    __tablename__ = 'hospital'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    speciality = db.Column(db.String(50),nullable=False)
    description = db.Column(db.Text,nullable=False)
    contact_no = db. Column(db.Integer,nullable=False)
    address = db.Column(db.Text,nullable=False)
    start_time = db.Column(db.Time,nullable=False)
    end_time = db.Column(db.Time,nullable=False)
    days = db.Column(db.PickleType,nullable=False)
    doctors_name = db.relationship('Doctors',secondary=relate, backref = db.backref('hospital', lazy = True))
    #services = db.Column(db.ARRAY(String))
    feedbacks = db.relationship('Feedback',backref='hospital')
    def __repr__(self):
        return f"Hospital Name is : {self.name}"

class Feedback(db.Model):
    __tablename__='feedback'
    id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(30),nullable=False)
    content = db.Column(db.Text,nullable=False)
    rating = db.Column(db.Integer,nullable=False)
    hosp_id = db.Column(db.Integer,db.ForeignKey('hospital.id'))

@login_manager.user_loader
def load_user(doctor_id):
    return Doctors.query.get(doctor_id)

class Doctors(db.Model, UserMixin):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20),nullable = False)
    password = db.Column(db.String(20))
    email = db.Column(db.String(64),unique = True,index = True)
    visiting_hours = db.Column(db.String(20),nullable = False)
    qualification = db.Column(db.String(50),nullable = False)
    specialization = db.Column(db.String(140))
    consultation_fees = db.Column(db.Integer, nullable = False)
    profile_image = db.Column(db.String(64),default = 'default_image.jpg')
    experience = db.Column(db.Text,nullable = False)
    contact_number = db.Column(db.String(10),nullable = False)
    description = db.Column(db.Text,nullable = False)
    hospitals_name = db.relationship('Hospitals',secondary=relate, backref = db.backref('doctor', lazy = True))
    def __init__(self,name,password,email,visiting_hours,qualification,specialization,consultation_fees,experience,contact_number,description):
        self.name = name
        self.password = password
        self.email = email
        self.visiting_hours = visiting_hours
        self.qualification = qualification
        self.specialization = specialization
        self.consultation_fees = consultation_fees
        self.experience = experience
        self.contact_number = contact_number
        self.description = description
    def check_password(self,password):
        return self.password==password
    def __repr__(self):
        return f"Name  : {self.name}"