from flask import render_template, request, Blueprint
from flask_login import current_user
from kindlycare import db
from kindlycare.models import Doctors, Hospitals, Feedback
from kindlycare.doctors.forms import FilterForm
core = Blueprint('core', __name__)


@core.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form.get('options'))  # Value of the Radio Button

    return render_template('index.html')


@core.route('/docs')
def docs():
    docs = Doctors.query.all()
    return render_template('home.html', docs=docs)


@core.route('/hosps')
def hosps():
    hosp = Hospitals.query.all()
    return render_template('home.html', hosp=hosp)


@core.route('/search')
def search():
    re = request.args.get("query")
    req = str(re).lower().split(" ")
    doc_list = []
    hosp_list = []
    docs = Doctors.query.all()
    hosp = Hospitals.query.all()
    for re in req:
        for d in docs:
            print(d.name)
            if re in d.name.lower().split(" ") or re in d.qualification.lower().split(" ") or re in d.specialization.lower().split(" "):
                doc_list.append(d)
        for h in hosp:
            if re in h.name.lower().split(" ") or re in h.speciality.lower().split(" "):
                hosp_list.append(h)
    return render_template('home.html', docs=doc_list, hosp=hosp_list)
