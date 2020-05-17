from wtforms import StringField, SubmitField, PasswordField, TextAreaField, IntegerField, SelectField
from flask_wtf import FlaskForm
# from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from kindlycare.models import Doctors


class DoctorsForms(FlaskForm):

    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    qualification = StringField(
        'Enter Your Qualification', validators=[DataRequired()])
    specialization = StringField(
        'Enter Your Specialization', validators=[DataRequired()])
    consultation_fees = IntegerField(
        'Consultation Fees', validators=[DataRequired()])
    experience = TextAreaField(
        'Enter Your Experience', validators=[DataRequired()])
    contact_number = StringField(
        'Enter Your Contact Number', validators=[DataRequired()])
    description = TextAreaField(
        'Enter a description of your', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    address_line_1 = TextAreaField(
        'Address_line_1', validators=[DataRequired()])
    address_line_2 = TextAreaField(
        'Address_line_2', validators=[DataRequired()])
    address_line_3 = TextAreaField(
        'Address_line_3', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        if Doctors.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


def filter_query():
    return Doctors.query


# class FilterForm(FlaskForm):
#     options = QuerySelectField(
#         query_factory=filter_query, allow_blank=True, get_label='specialization')


class UpdateForm(FlaskForm):
    email = StringField('Email')  # ,validators=[Email()])
    picture = FileField('Update Profile Picture')
    qualification = StringField('Qualification')
    specialization = StringField('Specialization')
    consultation_fees = IntegerField('Consultation Fees')
    experience = TextAreaField('Experience')
    description = TextAreaField('Description')
    address_line_1 = TextAreaField('Address line 1')
    address_line_2 = TextAreaField('Address line 2')
    address_line_3 = TextAreaField('Address line 3')
    submit = SubmitField('Update')


class ReviewForm(FlaskForm):
    name = StringField('Your name', validators=[DataRequired()])
    content = TextAreaField('Your feedback', validators=[DataRequired()])
    rating = SelectField('Your rating', validators=[DataRequired()], choices=[
                         ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    submit = SubmitField('Submit')
