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

@app.route('/admin_layouts')
def admin_layouts():
  return render_template("admin_layouts.html")


@app.route('/layouts')
def layouts():
  return render_template("layouts.html")


@app.route('/singleCourse')
def singleCourse():
  return render_template("singleCourse.html")

# @app.route('/login')
# def login():
#   return render_template("login.html")

@app.route('/loggedin')
def loggedin():
  return render_template("loggedin.html")

@app.route('/classSub')
def classSub():
  return render_template("classSub.html")


@app.route('/payGateway')
def payGateway():
  return render_template("payGateway.html")



@app.route('/admin_index')
def admin_index():
  return render_template("admin_index.html")

@app.route('/admin_stud_table')
def admin_stud_table():
  return render_template("admin_stud_table.html")

@app.route('/admin_teach_table')
def admin_teach_table():
  return render_template("admin_teach_table.html")

@app.route('/admin_teach_info')
def admin_teach_info():
  return render_template("admin_teach_info.html")


@app.route('/institute_index')
def institute_index():
  return render_template("institute_index.html")

@app.route('/inst_assign')
def inst_assign():
  return render_template("inst_assign.html")

@app.route('/inst_teach_table')
def inst_teach_table():
  return render_template("inst_teach_table.html")

@app.route('/inst_stud_table')
def inst_stud_table():
  return render_template("inst_stud_table.html")

@app.route('/admin_inst_table')
def admin_inst_table():
  return render_template("admin_inst_table.html")

@app.route('/admin_req_table')
def admin_req_table():
  return render_template("admin_req_table.html")

@app.route('/admin_inst_info')
def admin_inst_info():
  return render_template("admin_inst_info.html")

@app.route('/student_index')
def student_index():
  return render_template("student_index.html")

@app.route('/student_contact')
def student_contact():
  return render_template("student_contact.html")

@app.route('/student_about')
def student_about():
  return render_template("student_about.html")

@app.route('/student_courses')
def student_courses():
  return render_template("student_courses.html")




@app.route('/admin_stud_info')
def admin_stud_info():
  return render_template("admin_stud_info.html")


@app.route('/teacher_index')
def teacher_index():
  return render_template("teacher_index.html")

@app.route('/teach_req_table')
def teach_req_table():
  return render_template("teach_req_table.html")

@app.route('/teach_stud_table')
def teach_stud_table():
  return render_template("teach_stud_table.html")

@app.route('/teach_video')
def teach_video():
  return render_template("teach_video.html")

@app.route('/teach_inst_assign')
def teach_inst_assign():
  return render_template("teach_inst_assign.html")

@app.route('/register',methods=['GET','POST'])
def register():
 if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    address= request.form['address']
    contact= request.form['contact'] 
    age= request.form['age'] 
    disability = request.form['disability']
    my_data = Register(name=name,email=email,password=password,contact=contact,address=address,disability=disability,age=age,usertype="student")
    db.session.add(my_data) 
    db.session.commit()
    return redirect('/login')
 return render_template("register.html")


@app.route('/login',methods=['GET','POST'])
def login():
 if request.method=="POST":
    email=request.form['email']
    password=request.form['password']
    admin =Register.query.filter_by(email=email, password=password,usertype= 'admin').first()
    student =Register.query.filter_by(email=email, password=password,usertype= 'student').first()
    teacher =Register.query.filter_by(email=email, password=password,usertype= 'teacher').first()
    institute =Register.query.filter_by(email=email, password=password,usertype= 'institute').first()

    if admin:
      login_user(admin)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect('/admin_index') 
    
    elif student:

      login_user(student)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect('/student_index') 

    elif teacher:

      login_user(teacher)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect('/teacher_index')

    elif institute:

      login_user(institute)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect('/institute_index') 
 


    else:
      d="Invalid Username or Password!"
      return render_template("login.html",d=d)
 return render_template("login.html")

