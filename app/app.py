import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask import request, url_for,flash,redirect
from flask_user import current_user, login_required, roles_accepted
from flask.ext.login import login_user, logout_user, login_required,LoginManager
from forms import UserProfileForm
from user import User
import specifications as spec
app = Flask(__name__)
app.config.from_object(__name__)

lm = LoginManager()
lm.init_app(app)

@app.route('/')
def home():
    return render_template('profilepage.html')
@app.route('/login', methods=['GET', 'POST'])
def mainpage():
    form = UserProfileForm()

    # Process valid POST
    if request.method == 'POST' and form.validate_on_submit():
        usertab=spec['USER_COLLECTION'].find_one({'Username':form.username.data})
        if usertab and User.validate_login(usertab['Password'], form.password.data):
            user_obj = User(usertab['_id'])
            login_user(user_obj)
            flash("Logged in successfully!", category='success')
            return redirect(request.args.get("next") or url_for("write"))
        flash("Wrong username or password!", category='error')
    return render_template('templogin.html', title='login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)
def main():
    app.run('localhost',port=1010)
main()