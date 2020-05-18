from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import current_user
from kindlycare import db
from datetime import datetime,date
import calendar
from kindlycare.models import Slots,Reviews

# from kindlycare.doctors.forms import FilterForm
from kindlycare.models import Doctors, Hospitals, Feedback, Slots

core = Blueprint('core', __name__)

@core.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        opt = request.form.get('options')
        return redirect(url_for('core.filter', opt=opt))
    
    
    docs = []
    hosps = []
    hosps = Hospitals.query.limit(6).all()

    den_flag = 0
    ped_flag = 0
    gen_phy_flag = 0
    heart_flag = 0
    homeo_flag = 0
    neuro_flag = 0

    for doc in Doctors.query.all():
        if 'dentist' in doc.specialization.lower() and den_flag == 0:
            docs.append(doc)
            den_flag = 1
        
        if 'pediatrition' in doc.specialization.lower() and ped_flag == 0:
            docs.append(doc)
            ped_flag = 1
        
        if 'general physician' in doc.specialization.lower() and gen_phy_flag == 0:
            docs.append(doc)
            ped_flag = 1
        
        if 'homeopath' in doc.specialization.lower() and homeo_flag == 0:
            docs.append(doc)
            ped_flag = 1
        
        if 'neurologist' in doc.specialization.lower() and neuro_flag == 0:
            docs.append(doc)
            ped_flag = 1
        
        if 'heart' in doc.specialization.lower() and heart_flag == 0:
            docs.append(doc)
            ped_flag = 1

    return render_template('index.html', docs=docs, hosps=hosps)


@core.route('/about')
def about():
    return render_template('about.html')


@core.route('/filter')
def filter():
    docs = []
    opt = request.args.get('opt')
    for doc in Doctors.query.all():
        if opt.lower() in doc.specialization.lower():
            docs.append(doc)
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
            if re in d.name.lower() or re in d.qualification.lower() or re in d.specialization.lower():
                doc_list.append(d)
        for h in hosp:
            if re in h.name.lower() or re in h.speciality.lower():
                hosp_list.append(h)
    return render_template('home.html', docs=doc_list, hosp=hosp_list)
