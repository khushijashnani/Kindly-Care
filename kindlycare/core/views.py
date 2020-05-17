from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import current_user
from kindlycare import db

from kindlycare.doctors.forms import FilterForm
from kindlycare.models import Doctors, Hospitals, Feedback, Slots

core = Blueprint('core', __name__)


@core.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        opt = request.form.get('options')
        print(opt)  # Value of the Radio Button
        return redirect(url_for('core.filter', opt=opt))
    # print(current_user.slots.morning_slots)
    '''slot = Slots.query.filter_by(doc_id=current_user.id).all()
    for i in slot:
        print(i.morning_slots)'''
    docs = []
    hosps = []
    hosps = Hospitals.query.limit(6).all()
    print(hosps)
    docs.append(Doctors.query.filter_by(specialization='Dentist').first())
    docs.append(Doctors.query.filter_by(specialization='Pediatrition').first())
    docs.append(Doctors.query.filter_by(
        specialization='General Physician').first())
    docs.append(Doctors.query.filter_by(
        specialization='Heart Surgeon').first())
    docs.append(Doctors.query.filter_by(specialization='Homeopath').first())
    docs.append(Doctors.query.filter_by(specialization='Neurologist').first())

    docs = [i for i in docs if i]
    print(docs)
    return render_template('index.html', docs=docs, hosps=hosps)


@core.route('/about')
def about():
    return render_template('about.html')


@core.route('/filter')
def filter():
    opt = request.args.get('opt')
    docs = Doctors.query.filter_by(specialization=opt).all()
    return render_template('home.html', docs=docs)


@core.route('/docs')
def docs():
    if request.method == 'POST':
        opt = request.form.get('options')
        print(opt)  # Value of the Radio Button
        return redirect(url_for('core.filter', opt=opt))

    docs = Doctors.query.all()
    return render_template('home.html', docs=docs)


@core.route('/hosps')
def hosps():
    hosp = Hospitals.query.all()
    return render_template('home.html', hosp=hosp)


@core.route('/doctors')
def doctors():
    return render_template('doctors.html')


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
