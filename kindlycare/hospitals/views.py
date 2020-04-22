from flask import render_template,url_for,redirect,request,Blueprint,abort
from kindlycare.models import Hospitals
from kindlycare import db,app
from kindlycare.hospitals.forms  import HospitalForm

hosp = Blueprint('hospitals',__name__)

@app.route('/')
def home():
    return render_template('home.html')

@hosp.route('/form',methods=['GET','POST'])
def form():
    form = HospitalForm()
    if form.validate_on_submit():
        print("1")
        hosp = Hospitals(name=form.name.data,speciality=form.speciality.data,description=form.description.data,contact_no=form.contact.data,address=form.address.data,start_time=form.start_time.data,end_time=form.end_time.data,days=form.days.data)
        print("2")
        db.session.add(hosp)
        print("3")
        db.session.commit()
        print("123")
        for x in Hospitals.query.all():
            print(x.start_time)
            print(x.end_time)
            print(x.days)
        return render_template('home.html')
    return render_template('hform.html',form=form)