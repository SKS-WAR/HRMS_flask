# -*- coding: utf-8 -*-

from flask import Flask,redirect,url_for, render_template, request,send_file,session,flash
from flask_sqlalchemy import SQLAlchemy

import webbrowser
from datetime import datetime

app = Flask(__name__)
app.secret_key = "0d8fb9370a5bf7b892be4865cdf8b658a82209624e33ed71cae353b0df254a75db63d1baa35ad99f26f1b399c31f3c666a7fc67ecef3bdcdb7d60e8ada90b722"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#########################################################################################
class users(db.Model):
    _id = db.Column('id',db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    password =  db.Column(db.String(100))
    timestamp = db.Column(db.String(100))
    def __init__(self,name,passwrd,date):
        self.name = name
        self.password = passwrd
        self.timestamp = date
        
        
class employee(db.Model):
    uid = db.Column(db.Integer,primary_key=True)
    eid = db.Column(db.Integer)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    padrs = db.Column(db.String(100))
    tadrs = db.Column(db.String(100))
    dob = db.Column(db.String(100))
    c_no = db.Column(db.String(100))
    email = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    dept = db.Column(db.String(100))    
    deg = db.Column(db.String(100))
    blood_group = db.Column(db.String(100))
    edu_qua = db.Column(db.String(100))
    cert = db.Column(db.LargeBinary)
    ani = db.Column(db.String(100))
    religion = db.Column(db.String(100))
    driving_linc = db.Column(db.String(100))
    voter_id = db.Column(db.String(100))
    adhaar = db.Column(db.String(100))
    material_status = db.Column(db.String(100))
    photo = db.Column(db.LargeBinary)
    resume = db.Column(db.LargeBinary)
    doj = db.Column(db.String(100))
    def __init__(self,eid,fname,lname,padrs,tadrs,dob,c_no,email,gender,dept,deg,
                 blood_group,edu_qua,cert,ani,religion,driving_linc,voter_id,adhaar,
                 material_status,photo,resume,doj):
        self.eid = eid
        self.fname = fname
        self.lname = lname
        self.padrs = padrs
        self.tadrs = tadrs
        self.dob = dob
        self.c_no = c_no
        self.email = email
        self.gender = gender
        self.dept = dept
        self.deg = deg
        self.blood_group = blood_group
        self.edu_qua = edu_qua
        self.cert = cert
        self.ani = ani
        self.religion = religion
        self.driving_linc = driving_linc
        self.voter_id = voter_id
        self.adhaar = adhaar
        self.material_status = material_status
        self.photo = photo
        self.resume = resume
        self.doj = doj
        
#########################################################################################
    
@app.route("/",methods=["POST","GET"])
@app.route("/login",methods=["POST","GET"])
def login():
    if 'user' in session:
        if session['user'] != None:
            return redirect(url_for('home'))
    if request.method == "POST":
        uname = request.form["uname"]
        password = request.form["password"]
        found_user = users.query.filter_by(name = uname,password = password).first()
        if found_user:
            session['user'] = uname
            flash("Logged in successfully",category='success')
            return redirect(url_for('home'))
        else:
            flash("Invalid Email and password",category='error')
            return render_template('login.html')
    else:
        return render_template("login.html")
    
@app.route("/register",methods=["POST","GET"])
def register():
    if 'user' in session:
        if session['user'] != None:
            return redirect(url_for('home'))
    if request.method == "POST":
        uname = request.form["uname"]
        password = request.form["password"]
        now = datetime.now().date()
        new_user = users(name = uname,passwrd=password,date=str(now))
        db.session.add(new_user)
        db.session.commit()
        found_user = users.query.filter_by(name = uname,password = password).first()
        if found_user:
            session['user'] = uname
            flash("Logged in successfully",category='success')
            return render_template("registerAdmin.html")
        else:
            flash("Invalid Email and password",category='error')
            return render_template('registerAdmin.html')
    else:
        return render_template("registerAdmin.html")
    
    
    
    
@app.route("/home")
def home():
    return render_template('home.html')
    
@app.route("/createEmployee",methods=["POST","GET"])
def createEmployee():
    return render_template('createEmployee.html')
    
@app.route("/logout")
def logout(): 
    session.pop('patient',None)
    session.pop('user',None)
    return redirect(url_for('login'))


#######################################################################################

if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:5000/')
    db.create_all()
    app.run()