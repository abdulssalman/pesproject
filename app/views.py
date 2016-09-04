from flask import Flask, render_template
from flask import request, url_for,flash,redirect
from flask_login import login_user, logout_user, LoginManager
from pymongo import MongoClient
from flask_pymongo import PyMongo
from app import app
# import specifications as spec
from forms  import UserProfileForm,UserProfileForm2
from werkzeug.security import generate_password_hash
from user  import User
__name__='views'
app = Flask(__name__)
print __name__
app.secret_key='my secret'
app.config.from_object(__name__)

mongo=PyMongo(app,)
lm = LoginManager()
lm.init_app(app)
app.config['MONGO_DBNAME']='UserData'
print app.config['MONGO_DBNAME']
# db=cx['UserData']
# mongo=mongo.init_app(app,config_prefix='UserData')

@app.route('/')
def home():
    return render_template('index2.html')
@app.route('/login', methods=['GET', 'POST'])
def indexpage():
    form = UserProfileForm()

    # Process valid POST
    if request.method == 'POST' :
        # print app.config['USER_COLLECTION'].find_one()
        usertab=mongo.db.users.find_one({'Username':str(form.username.__class__ )})
        print str(form.username)
        if usertab and User.validate_login(usertab['Password'], form.password.data):
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
        if form2.password.data==form2.confirm_password.data:
            pass_hash = generate_password_hash(form2.password.data, method='pbkdf2:sha256')
            mongo.db.users.insert({'Username':str(form2.email),'Password':pass_hash})
            flash( "user Successfully Registered",category='success')
            return redirect('index2.html',title='login',form =form2)
        else:
            print 'mismatch'
    return render_template('index2.html', title='login', form=form2)

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
def main():
    app.run('localhost', port=1010)
main()

