from flask import render_template, request, Blueprint
from kindlycare.models import User

core = Blueprint('core', __name__)


@core.route('/')
def home():
    print(User.query.all())
    return render_template('home.html')


