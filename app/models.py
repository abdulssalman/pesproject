from flask_user import UserMixin
from flask_user.forms import RegisterForm
from flask_wtf import Form
from wtforms import StringField,SubmitField,validators
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from app import app
db=PyMongo(app)

login_manager=LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)