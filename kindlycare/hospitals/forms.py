from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,IntegerField,TextAreaField,TextField,TimeField,SelectMultipleField,SelectField
from wtforms.validators import DataRequired

class HospitalForm(FlaskForm):
    doctor_name = StringField('Enter Your name as mentioned in previous form',validators=[DataRequired()])
    name = StringField(label='Enter Hospital name:',validators=[DataRequired()])
    speciality = StringField('Enter speciality:',validators=[DataRequired()])
    description = TextAreaField('Enter description:',validators=[DataRequired()])
    contact_no = IntegerField('Enter centers contact no: ',validators=[DataRequired()])
    address = TextField('Enter the location of the center: ',validators=[DataRequired()])
    start_time = TimeField('Starting time:',validators=[DataRequired()])
    end_time = TimeField('Closing time:',validators=[DataRequired()])
    days = SelectMultipleField('Working Days:', choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thurs', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')],validators=[DataRequired()])
    submit = SubmitField('Submit')

class FeedBackForm(FlaskForm):
    user_name = StringField('Your name',validators=[DataRequired()])
    content = TextAreaField('Your feedback',validators=[DataRequired()])
    rating = SelectField('Your rating',validators=[DataRequired()],choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    submit = SubmitField('Submit') 