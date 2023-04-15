from flask import Flask, render_template, request, redirect, flash, abort, url_for, session
from starter import app
from starter import app
from starter.models import *
from flask_login import login_user, current_user, logout_user, login_required
from random import randint
import os



@app.route('/',methods=['GET', 'POST'])
def index():
 return render_template("index.html")


@app.route('/user_index',methods=['GET', 'POST'])
def user_index():
 return render_template("user_index.html")


@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/home')
def home():
  return render_template("index.html")

@app.route('/courses')
def courses():
  return render_template("courses.html")

@app.route('/contact')
def contact():
  return render_template("contact.html")

@app.route('/layouts')
def layouts():
  return render_template("layouts.html")

@app.route('/singleCourse')
def singleCourse():
  return render_template("singleCourse.html")

@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/loggedin')
def loggedin():
  return render_template("loggedin.html")

@app.route('/classSub')
def classSub():
  return render_template("classSub.html")


@app.route('/payGateway')
def payGateway():
  return render_template("payGateway.html")




@app.route('/register',methods=['GET','POST'])
def register():
 if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    address= request.form['address']
    contact= request.form['contact'] 
    my_data = Register(name=name,email=email,password=password,contact=contact,address=address,usertype="user")
    db.session.add(my_data) 
    db.session.commit()
    return redirect('/login')
 return render_template("register.html")


# @app.route('/login',methods=['GET','POST'])
# def login():
#  if request.method=="POST":
#     email=request.form['email']
#     password=request.form['password']
#     admin =Register.query.filter_by(email=email, password=password,usertype= 'admin').first()
#     user =Register.query.filter_by(email=email, password=password,usertype= 'user').first()

#  if admin:
#   login_user(admin)
#   next_page = request.args.get('next')
#   return redirect(next_page) if next_page else redirect('/admin_index') 
 
#  elif user:

#   login_user(user)
#   next_page = request.args.get('next')
#   return redirect(next_page) if next_page else redirect('/user_index') 

#  else:
#   d="Invalid Username or Password!"
#   return render_template("login.html",d=d)
#  return render_template("login.html")

