# from flask import Blueprint, render_template, url_for, request, redirect, flash
# from flask_login import login_user, current_user, logout_user, login_required
# from kindlycare import db
# from kindlycare.models import User
# from kindlycare.users.forms import RegistrationForm, LoginForm, UpdateUserForm


# users = Blueprint('users', __name__)



# @users.route('/register', methods=['GET', 'POST'])
# def register():

#     form = RegistrationForm()

#     if form.validate_on_submit():
#         user = User(name=form.name.data, email=form.email.data,
#                     password=form.password.data)

#         db.session.add(user)
#         db.session.commit()

#         flash('Thanks for registration!')
#         return redirect(url_for('core.home'))

#     return render_template('register.html', form=form)

# @users.route('/login', methods=['GET', 'POST'])
# def login():

#     form = LoginForm()
#     if form.validate_on_submit():

#         user = User.query.filter_by(email=form.email.data).first()

#         if user is not None and user.check_password(form.password.data):
#             login_user(user)
#             flash('Login Success')

#             next = request.args.get('next')

#             if next == None or not next[0] == '/':
#                 next = url_for('core.home')

#             return redirect(next)

#     return render_template('login.html', form=form)

# @users.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('core.home'))