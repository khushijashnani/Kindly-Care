import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'practo'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
app.config['DEBUG'] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kay1872k@gmail.com'
app.config['MAIL_PASSWORD'] = 'KayJashnani18k'
app.config['MAIL_DEFAULT_SENDER'] = 'kay1872k@gmail.com'
app.config['MAIL_ASCII_ATTACHMENTS'] = False
app.config['MAIL_MAX_EMAILS'] = None



db = SQLAlchemy(app)
Migrate(app, db)
mail = Mail(app)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'doctors.login'

#from kindlycare.users.views import users
from kindlycare.core.views import core
from kindlycare.hospitals.views import hospitals
from kindlycare.doctors.views import doctors

app.register_blueprint(core)
#app.register_blueprint(users)
app.register_blueprint(hospitals)
app.register_blueprint(doctors)

