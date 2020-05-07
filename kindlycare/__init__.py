
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SECRET_KEY'] = 'practo'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

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
