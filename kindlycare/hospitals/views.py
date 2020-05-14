from flask import render_template,url_for,redirect,request,Blueprint,abort,flash
from kindlycare.models import Hospitals,Doctors,Feedback,Slots,Appointments
from kindlycare import db,app,mail
from flask_mail import Message
from kindlycare.hospitals.forms  import HospitalForm,FeedBackForm,AppointmentForm
from flask_login import login_required,current_user


hospitals = Blueprint('hospitals',__name__)

@hospitals.route('/hosp<int:hosp_id>',methods=['GET','POST'])
def hosp(hosp_id):
    hosp = Hospitals.query.get_or_404(hosp_id)
    feed = Feedback.query.filter_by(hosp_id=hosp_id).all()
    form = FeedBackForm()
    slots = Slots.query.filter_by(hospital_name=hosp.name).all()

    if form.validate_on_submit():
        feedback = Feedback(user_name=form.user_name.data,content=form.content.data,rating=form.rating.data,hosp_id=hosp_id)
        db.session.add(feedback)
        db.session.commit()
        flash('Thank you for your feedback!','success')
        return redirect(url_for('hospitals.hosp',hosp_id=hosp_id))
    return render_template('hospital.html',hosp=hosp,form=form,feed=feed,slots=slots)
    

@hospitals.route('/appoint/<int:slot_id>/<string:c>',methods=['GET','POST'])
def appoint(slot_id,c):
    slot = Slots.query.filter_by(id=slot_id).first()
    form = AppointmentForm()
    if c == 'morning' :
        form.slot.choices = [(x,x) for x in slot.morning_slots.split(",") if "-" in x]
        form.day.choices = [(x,x) for x in slot.morning_slots.split(",") if "-" not in x]
    if c == 'afternoon' :
        form.slot.choices = [(x,x) for x in slot.afternoon_slots.split(",") if "-" in x]
        form.day.choices = [(x,x) for x in slot.afternoon_slots.split(",") if "-" not in x ]
    if c == 'evening' :
        form.slot.choices = [(x,x) for x in slot.evening_slots.split(",") if "-" in x]
        form.day.choices = [(x,x) for x in slot.evening_slots.split(",") if "-" not in x]
    if c == 'night' : 
        form.slot.choices = [(x,x) for x in slot.night_slots.split(",") if "-" in x]
        form.day.choices = [(x,x) for x in slot.night_slots.split(",") if "-" not in x]
    if form.validate_on_submit():
        appointment = Appointments(slot=form.slot.data,day=form.day.data,user_email=form.user_email.data,hosp_name=slot.hospital_name,doc_id=slot.doc_id)
        if c == 'morning' :
            slot.m_capacity += 1
        if c == 'afternoon' :
            slot.a_capacity += 1
        if c == 'evening' :
            slot.e_capacity += 1
        if c == 'night' : 
            slot.n_capacity += 1
        db.session.add(appointment)
        db.session.commit()
        msg = Message(subject='Appointment Confirmation from Kindly-Care',body='Your appointment at '+appointment.hosp_name+', is confirmed in the slot '+appointment.slot+'on'+appointment.day+'. Thank you.',recipients=[appointment.user_email])
        mail.send(msg)
        print(slot.e_capacity)
        print(appointment.slot)
        print(appointment.day)
        print(appointment.doc_id)
        print(appointment.hosp_name)
        flash('Your appointment has been booked! Please check your mail.','success')
        return redirect(url_for('doctors.viewDoctor',doctor_id=slot.doc_id))
    return render_template('appointment.html',form=form)

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
        print(doctor.id)

        if form.name.data in hospital_names:
            hosp = Hospitals.query.filter_by(name=form.name.data).first()
            hosp.doctors_name.append(doctor)
            slot = Slots(doc_id=doctor.id,morning_slots=form.morning_slots.data,afternoon_slots=form.afternoon_slots.data,evening_slots=form.evening_slots.data,night_slots=form.night_slots.data,hospital_name=form.name.data)
            db.session.add(slot)
            db.session.commit()

            return redirect(url_for('core.home'))

        hosp = Hospitals(name=form.name.data,speciality=form.speciality.data,description=form.description.data,contact_no=form.contact_no.data,address=form.address.data,start_time=form.start_time.data,end_time=form.end_time.data,days=form.days.data)
        hosp.doctors_name.append(doctor)
        slot = Slots(doc_id=doctor.id,morning_slots=form.morning_slots.data,afternoon_slots=form.afternoon_slots.data,evening_slots=form.evening_slots.data,night_slots=form.night_slots.data,hospital_name=form.name.data)
        db.session.add(slot)
        db.session.add(hosp)
        db.session.commit()
        
        for x in Hospitals.query.all():
            print(x.start_time)
            print(x.end_time)
            print(x.days)
        return redirect(url_for('core.home'))
        
    return render_template('hform.html',form=form)