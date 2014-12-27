import os
from flask import Flask, request, flash, url_for, redirect, \
render_template, abort, send_from_directory, \
session, make_response, jsonify


app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')
from constants import MYSQL_URI
app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_URI


@app.route('/')
def index():
    return 'Hello World!'

@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)



#Importing forms, preventing a CSRF attack
from forms import SignupForm, SigninForm
from models import db, Administrador
db.init_app(app)


@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'


@app.route('/home')
def home():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
 
  user = Administrador.query.filter_by(email = session['email']).first()
 
  if user is None:
    return redirect(url_for('signin'))
  else:
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:   
      newuser = Administrador(form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()

      #Saving session variable 
      session['email'] = newuser.email

      #return "[1] Create a new user [2] sign in the user [3] redirect to the user's home"
      return redirect(url_for('home'))
   
  elif request.method == 'GET':
    return render_template('signup.html', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
  form = SigninForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signin.html', form=form)
    else:
      session['email'] = form.email.data
      return redirect(url_for('home'))
                 
  elif request.method == 'GET':
    return render_template('signin.html', form=form)


@app.route('/signout')
def signout():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
     
  session.pop('email', None)
  return redirect(url_for('index'))



@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

    if __name__ == '__main__':
        app.run()