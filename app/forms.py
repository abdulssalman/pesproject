from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class UserProfileForm:
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
class UserProfileForm2:
    email=StringField('Email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('ConfirmPassword',validators=[DataRequired()])