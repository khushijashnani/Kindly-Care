from flask import render_template,url_for,redirect,request,Blueprint,abort,flash
from kindlycare.models import Hospitals,Doctors,Feedback
from kindlycare import db,app
from kindlycare.hospitals.forms  import HospitalForm,FeedBackForm
from flask_login import login_required


hospitals = Blueprint('hospitals',__name__)

@hospitals.route('/hosp<int:hosp_id>',methods=['GET','POST'])
def hosp(hosp_id):
    hosp = Hospitals.query.get_or_404(hosp_id)
    feed = Feedback.query.filter_by(hosp_id=hosp_id).all()
    form = FeedBackForm()
    if form.validate_on_submit():
        feedback = Feedback(user_name=form.user_name.data,content=form.content.data,rating=form.rating.data,hosp_id=hosp_id)
        db.session.add(feedback)
        db.session.commit()
        flash('Thank you for your feedback!','success')
        return redirect(url_for('hospitals.hosp',hosp_id=hosp_id))
    return render_template('hospital.html',hosp=hosp,form=form,feed=feed)

@login_required
@hospitals.route('/hospital_form',methods=['GET','POST'])
def register_hospital():
    form = HospitalForm()

    if form.validate_on_submit():

        hospital_names=[]
        for hospital in Hospitals.query.all():
            hospital_names.append(hospital.name)
        
        doctor_name = form.doctor_name.data
        doctor = Doctors.query.filter_by(name=doctor_name).first()

        if form.name.data in hospital_names:
            hosp = Hospitals.query.filter_by(name=form.name.data).first()
            hosp.doctors_name.append(doctor)
            db.session.commit()

            return redirect(url_for('core.home'))

        hosp = Hospitals(name=form.name.data,speciality=form.speciality.data,description=form.description.data,contact_no=form.contact_no.data,address=form.address.data,start_time=form.start_time.data,end_time=form.end_time.data,days=form.days.data)
        hosp.doctors_name.append(doctor)
        db.session.add(hosp)
        db.session.commit()
        
        for x in Hospitals.query.all():
            print(x.start_time)
            print(x.end_time)
            print(x.days)
        return redirect(url_for('core.home'))
        
    return render_template('hform.html',form=form)