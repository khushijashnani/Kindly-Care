from flask import render_template, request, Blueprint
from flask_login import current_user
#from kindlycare.models import User
from kindlycare.models import Doctors,Hospitals

core = Blueprint('core', __name__)


@core.route('/')
def home():
    # print(Doctors.query.all())
    # print(current_user.hospitals_name)
    # print(Hospitals.query.all())
    return render_template('home.html')


