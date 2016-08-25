# -*- coding: utf-8 -*-
import bottle
from bottle import static_file,app


@bottle.route('/')
# def staticFiles():
#     return static_file('main.js',root='./static/')
# def my_home():
#     stuff=['kakka','shit','sundas','poop']
#     return static_file('profilepage.html','./public')
# def my_homecss1():
#     return static_file('style.css','./public')
# def my_homecss2():
#     return static_file('own.css','./public/assets/css')
# def my_homejs4():
#     return static_file('own.js','./public/assets/js')
# def my_homejs5():
#     return static_file('bootstrap.min.js','./public/assets/js')
# def my_homejs6():
#     return static_file('jquery.min.js','./public/assets/js')
#
# def my_homejs1():
#     return static_file('main.js','./public')
# def my_homejs2():
#     return static_file('own.js','./public')
def my_homejs3():
    return bottle.template('index.html')
@bottle.get('/style.css')
# def styleSheets(style):
#     return static_file('{}.css' .format(style),root='static/')


#    return bottle.template('home_page.tpl',username='Krishna','things'=stuff})
# @bottle.post('/publicjs')
# def whatShit():
#     data=bottle.request.forms.get("shit")
#     print data
#     bottle.response.set_cookie("shit",data)
#     bottle.redirect("/publicjs")
# @bottle.route("/showShit")
# def showShit():
#     shitName=bottle.request.get_cookie("shit")
#     return bottle.template('shitSelection.tpl',{'shitSelected':shitName})

#    return '<html><head><title>this is shit</title></head><body> <h1>welcome to my world</body></html>'
@bottle.route('/test')
def my_testroom():
    return 'U r in the room'
bottle.debug(True)
bottle.run(host='localhost',port=8070)






# -*- coding: utf-8 -*-

