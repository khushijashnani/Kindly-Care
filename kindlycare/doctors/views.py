from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_login import login_user, current_user, logout_user, login_required
from kindlycare import db
from kindlycare.models import Doctors,Hospitals,Reviews,Slots
from kindlycare.doctors.forms import DoctorsForms,LoginForm,UpdateForm,ReviewForm
from kindlycare.doctors.picture_handler import add_profile_pic

doctors = Blueprint('doctors', __name__)

@doctors.route('/register',methods = ['GET','POST'])
def register():
	form = DoctorsForms()

	if form.validate_on_submit():

		print(form.name.data)

		doctor = Doctors(name=form.name.data,
						password=form.password.data,
						email=form.email.data,
						qualification=form.qualification.data,
						specialization=form.specialization.data,
						consultation_fees=form.consultation_fees.data,
						experience=form.experience.data,
						contact_number=form.contact_number.data,
						description=form.description.data,
						address_line_1=form.address_line_1.data,
						address_line_2=form.address_line_2.data,
						address_line_3=form.address_line_3.data)
						
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


@login_required
@doctors.route('/account',methods=['GET','POST'])
def update_doctor():

	print(current_user.email)
	form = UpdateForm()

	if request.method == 'POST':
		print('hello')
		if form.picture.data:
			print('hello')
			user_name = current_user.name
			pic = add_profile_pic(form.picture.data,user_name)
			current_user.profile_image = pic

		current_user.email = form.email.data
		current_user.experience = form.experience.data
		current_user.qualification = form.qualification.data
		current_user.specialization = form.specialization.data
		current_user.consultation_fees = form.consultation_fees.data
		current_user.description = form.description.data
		current_user.address_line_1 = form.address_line_1.data
		current_user.address_line_2 = form.address_line_2.data
		current_user.address_line_3 = form.address_line_3.data

		db.session.commit()
		flash('User Account Updated!!')
		return redirect(url_for('doctors.update_doctor'))

	elif request.method == 'GET':
		form.email.data = current_user.email
		form.experience.data = current_user.experience
		form.qualification.data = current_user.qualification
		form.specialization.data = current_user.specialization
		form.consultation_fees.data = current_user.consultation_fees
		form.description.data = current_user.description
		form.address_line_1.data = current_user.address_line_1
		form.address_line_2.data = current_user.address_line_2
		form.address_line_3.data = current_user.address_line_3
	
	else:
		print('error')
	
	profile_image = url_for('static',filename='profile_pics/'+current_user.profile_image)
	return render_template('account.html',form=form,profile_image=profile_image)


@doctors.route('/doctor<int:doctor_id>',methods=['GET','POST'])
def viewDoctor(doctor_id):
	doc = Doctors.query.filter_by(id=doctor_id).first()
	address = doc.address_line_1+', '+doc.address_line_2+', '+doc.address_line_3
	reviews = Reviews.query.filter_by(doctor_id=doc.id).all()
	slots = Slots.query.filter_by(doc_id=doctor_id).all()
	for slot in slots:
		print(slot.hospital_name)
	form = ReviewForm()

	if form.validate_on_submit():
		review = Reviews(name=form.name.data,content=form.content.data,rating=form.rating.data,doctor_id=doctor_id)
		db.session.add(review)
		db.session.commit()
		flash('Thank you for your feedback!','success')
		return redirect(url_for('doctors.viewDoctor',doctor_id=doctor_id))
	return  render_template('doctors.html',doc=doc,address = address,reviews=reviews,form=form,slots=slots)