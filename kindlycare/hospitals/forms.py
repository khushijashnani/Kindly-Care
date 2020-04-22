from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,IntegerField,TextAreaField,TextField,TimeField,SelectMultipleField
from wtforms.validators import DataRequired

class HospitalForm(FlaskForm):
    name = StringField(label='Enter your name:',validators=[DataRequired()])
    speciality = StringField('Enter speciality:',validators=[DataRequired()])
    description = TextAreaField('Enter description:',validators=[DataRequired()])
    contact = IntegerField('Enter centers contact no: ',validators=[DataRequired()])
    address = TextField('Enter the location of the center: ',validators=[DataRequired()])
    start_time = TimeField('Starting time:',validators=[DataRequired()])
    end_time = TimeField('Closing time:',validators=[DataRequired()])
    days = SelectMultipleField('Working Days:', choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thurs', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')],validators=[DataRequired()])
    submit = SubmitField('Submit')