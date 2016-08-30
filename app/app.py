import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_socketio import SocketIO  
from flask_socketio import send, emit   


app = Flask(__name__)
app.config.from_object(__name__)
socketio = SocketIO(app)


@app.route('/')
def main():
    return render_template('mainpage.html') 

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
    
if __name__ == '__main__':
    socketio.run(app)   
app.config.from_envvar('FLASKR_SETTINGS', silent=True)     