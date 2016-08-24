import bottle
import pymongo
from bottle import static_file
@bottle.route('/static/style.css')
def server_static(style):
    return static_file(style,root='C:\Users\Krishna\Desktop\Projects\pesproject\app\static')
@bottle.route('/')
def index_page():
    return bottle.template('index.tpl')
bottle.debug(True)
bottle.run(host='localhost',port=8000)
