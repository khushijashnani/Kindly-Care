from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_login import login_user, current_user, logout_user, login_required
from kindlycare import db
from kindlycare.models import Doctors,Hospitals
from kindlycare.doctors.forms import DoctorsForms,LoginForm

doctors = Blueprint('doctors', __name__)

@doctors.route('/register',methods = ['GET','POST'])
def register():
	form = DoctorsForms()

	if form.validate_on_submit():

		print(form.name.data)

		doctor = Doctors(name=form.name.data,
						password=form.password.data,
						email=form.email.data,
						visiting_hours=form.visiting_hours.data,
						qualification=form.qualification.data,
						specialization=form.specialization.data,
						consultation_fees=form.consultation_fees.data,
						experience=form.experience.data,
						contact_number=form.contact_number.data,
						description=form.description.data)
						
		db.session.add(doctor)
		db.session.commit()

		print(form.email.data)
		
		return redirect(url_for('hospitals.register_hospital'))

	return render_template('register.html',form=form)


@doctors.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        doctor = Doctors.query.filter_by(email=form.email.data).first()

        if doctor is not None and doctor.check_password(form.password.data):
            login_user(doctor)
            flash('Login Success')

            return redirect(url_for('core.home'))

    return render_template('login.html', form=form)

@doctors.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.home'))
