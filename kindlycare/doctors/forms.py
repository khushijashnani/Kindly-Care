from wtforms import StringField, SubmitField, PasswordField, TextAreaField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from kindlycare.models import Doctors

class DoctorsForms(FlaskForm):
    name = StringField('Name',validators = [DataRequired()])
    email = StringField('Email',validators = [DataRequired(),Email()])
    visiting_hours = StringField('Visiting Hours',validators = [DataRequired()])
    qualification = StringField('Enter Your Qualification',validators = [DataRequired()])  
    specialization = StringField('Enter Your Specialization',validators = [DataRequired()]) 
    consultation_fees = IntegerField('Consultation Fees',validators = [DataRequired()])
    experience = TextAreaField('Enter Your Experience',validators = [DataRequired()])
    contact_number = StringField('Enter Your Contact Number',validators = [DataRequired()])
    description = TextAreaField('Enter a description of your',validators = [DataRequired()])
    password = PasswordField('Password',validators = [DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        if Doctors.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class FilterForm(FlaskForm):