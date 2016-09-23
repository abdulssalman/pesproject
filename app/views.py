from flask import Flask, render_template
from flask import request, url_for,flash,redirect
from flask_login import login_user, logout_user, LoginManager
from pymongo import MongoClient
from flask_pymongo import PyMongo
# from app import app,lm
# import specifications as spec
from forms  import UserProfileForm,UserProfileForm2
from werkzeug.security import generate_password_hash
from user  import User
import os
import sqlite3
from flask import  request, session, g, abort
from flask_socketio import SocketIO
from flask_socketio import send, emit

app = Flask(__name__)
app.secret_key='my secret'
app.config.from_object(__name__)
socketio = SocketIO(app)



# connection=MongoClient('localhost',27017)
# db=connection.views
# collect=db.users

mongo=PyMongo(app)
lm = LoginManager()
lm.init_app(app)
app.config['MONGO_DBNAME']='UserData'
# mongo.db
# mongo.db.users
# print app.config['MONGO_DBNAME']
# db=cx['UserData']
# mongo=mongo.init_app(app,config_prefix='UserData')

@app.route('/')
def home():
    return render_template('index2.html')
@app.route('/chat')
def main1():
    return render_template('mainpage2.html')

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')



@app.route('/login', methods=['GET', 'POST'])
def indexpage():
    form = UserProfileForm()
    # Process valid POST
    if request.method == 'POST' :
        print "I am here"
        # print app.config['USER_COLLECTION'].find_one()
        usertab=mongo.db.users.find_one({'Username':(str(form.username).encode()) })
        print usertab,(form.username)
        if usertab and User.validate_login(usertab['Password'], str(form.password).encode()):
            user_obj = User(usertab['_id'])
            login_user(user_obj)
            flash("Logged in successfully!", category='success')
            return redirect(request.args.get("next") or url_for("mainpage"))
        print ("Wrong username or password!")
    return render_template('index2.html', title='login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def indexpage2():

    form2 = UserProfileForm2()
    if request.method=='POST':
        if str(form2.password).encode()==str(form2.confirm_password).encode():
            pass_hash = generate_password_hash(str(form2.password).encode(), method='pbkdf2:sha256')
            mongo.db.users.insert({'Username':str(form2.email).encode(),'Password':pass_hash})
            flash( "user Successfully Registered",category='success')
            return redirect('index2.html',title='register',form =form2)
        else:
            print 'mismatch'
    return render_template('index2.html', title='register', form=form2)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
# @lm.user_loader
# def load_user(username):
#     u = app.config['USER_COLLECTION'].find_one({"Username": form.username.data})
#     if not u:
#         return None
#     return User(u['_id'])
# # app.config.from_envvar('FLASKR_SETTINGS', silent=True)
if __name__ == '__main__':
    socketio.run(app,host='localhost',port=1500)
    # app.config.from_envvar('FLASKR_SETTINGS', silent=True)main()