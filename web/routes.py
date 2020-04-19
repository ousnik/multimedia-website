from flask import render_template, url_for, redirect, abort
from web import app
from web.tutorial_details import tut_list,path

@app.route('/')
@app.route('/home')
def home():
   return render_template('home.html', title='Home', tut_list=tut_list)

@app.route('/tutorials/<int:id>')
def tutorial(id):
  if id in range(1,11):
    topic=" - "+tut_list[id-1]
    return render_template('tutorial.html', title="Tutorial "+str(id), num=id, topic=topic, path=path[id-1])
  else:
    abort(404)
