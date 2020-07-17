# -*- coding: utf-8 -*-

from flask import Flask,redirect,url_for, render_template, request,send_file,session,flash
from flask_sqlalchemy import SQLAlchemy

import webbrowser
from datetime import datetime
from io import BytesIO

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
    father_name = db.Column(db.String(100))
    padrs = db.Column(db.String(100))
    pcity = db.Column(db.String(100))
    p_pin = db.Column(db.String(100))
    tadrs = db.Column(db.String(100))
    tcity = db.Column(db.String(100))
    t_pin = db.Column(db.String(100))
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
    def __init__(self,eid,fname,lname,father_name,padrs,pcity,p_pin,tadrs,tcity,t_pin,dob,c_no,email,
                 gender,dept,deg,blood_group,edu_qua,cert,ani,religion,driving_linc,voter_id,adhaar,
                 material_status,photo,resume,doj):
        self.eid = eid
        self.fname = fname
        self.lname = lname
        self.father_name = father_name
        self.padrs = padrs
        self.pcity = pcity
        self.p_pin = p_pin
        self.tadrs = tadrs
        self.tcity = tcity
        self.t_pin = t_pin
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

class ex_employee(db.Model):
    uid = db.Column(db.Integer,primary_key=True)
    eid = db.Column(db.Integer)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    father_name = db.Column(db.String(100))
    padrs = db.Column(db.String(100))
    pcity = db.Column(db.String(100))
    p_pin = db.Column(db.String(100))
    tadrs = db.Column(db.String(100))
    tcity = db.Column(db.String(100))
    t_pin = db.Column(db.String(100))
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
    def __init__(self,eid,fname,lname,father_name,padrs,pcity,p_pin,tadrs,tcity,t_pin,dob,c_no,email,
                 gender,dept,deg,blood_group,edu_qua,cert,ani,religion,driving_linc,voter_id,adhaar,
                 material_status,photo,resume,doj):
        self.eid = eid
        self.fname = fname
        self.lname = lname
        self.father_name = father_name
        self.padrs = padrs
        self.pcity = pcity
        self.p_pin = p_pin
        self.tadrs = tadrs
        self.tcity = tcity
        self.t_pin = t_pin
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

class date_status(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    eid = db.Column(db.Integer)
    date = db.Column(db.String(100))
    status = db.Column(db.String(10))
    def __init__(eid,date,status):
        self.eid = eid
        self.date = date
        self.status = status

class daily_io(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    eid = db.Column(db.Integer)
    date = db.Column(db.String(100))
    in_time = db.Column(db.String(100))
    out_time = db.Column(db.String(100))
    status = db.Column(db.String(10))
    def __init__(eid,date,in_time,out_time):
        self.eid = eid
        self.date = date
        self.in_time = in_time
        self.out_time = out_time

class lunch_io(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    eid = db.Column(db.Integer)
    date = db.Column(db.String(100))
    in_time = db.Column(db.String(100))
    out_time = db.Column(db.String(100))
    status = db.Column(db.String(10))
    def __init__(eid,date,in_time,out_time):
        self.eid = eid
        self.date = date
        self.in_time = in_time
        self.out_time = out_time

class tea_io(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    eid = db.Column(db.Integer)
    date = db.Column(db.String(100))
    in_time = db.Column(db.String(100))
    out_time = db.Column(db.String(100))
    status = db.Column(db.String(10))
    def __init__(eid,date,in_time,out_time):
        self.eid = eid
        self.date = date
        self.in_time = in_time
        self.out_time = out_time
        
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
            flash("Invalid Email and password",category='danger')
            return render_template('registerAdmin.html')
    else:
        return render_template("registerAdmin.html")
    
    
    
    
@app.route("/home")
def home():
    return render_template('home.html')
    
@app.route("/createEmployee",methods=["POST","GET"])
def createEmployee():
    if 'user' in session :
        pass
    if request.method == "POST":
        eid = request.form['eid']
        fname = request.form['fname']
        lname = request.form['lname']
        father_name = request.form['father_name']
        padrs = request.form['padrs']
        pcity = request.form['pcity']
        p_pin = request.form['p_pin']
        tadrs = request.form['tadrs']
        tcity = request.form['tcity']
        t_pin = request.form['t_pin']
        dob = request.form['dob']
        c_no = request.form['c_no']
        email = request.form['email']
        gender = request.form['gender']
        dept = request.form['dept']
        deg = request.form['deg']
        blood_group = request.form['blood_group']
        edu_qua = request.form['edu_qua']
        cert = request.files['cert']
        ani = request.form['ani']
        religion = request.form['religion']
        driving_linc = request.form['driving_linc']
        voter_id = request.form['voter_id']
        adhaar = request.form['adhaar']
        photo = request.files['photo']
        material_status = request.form['material_status']
        resume = request.files['resume']
        doj = request.form['doj']
        new_employee = employee(eid, fname, lname, father_name, padrs, pcity, p_pin,
         tadrs, tcity, t_pin, dob, c_no, email, gender, dept, deg, blood_group,
          edu_qua, cert.read(), ani, religion, driving_linc, voter_id, adhaar, material_status,
           photo.read(), resume.read(), doj)
        db.session.add(new_employee)
        db.session.commit()
        flash("Successfully Added the New Employee",category='success')
        return render_template('createEmployee.html')
    else:
        return render_template('createEmployee.html')
    
@app.route("/updateEmployee",methods=["POST","GET"])
def updateEmployee():
    if 'user' in session :
        pass
    if request.method == "POST":
        eid = request.form['eid']
        fname = request.form['fname']
        lname = request.form['lname']
        father_name = request.form['father_name']
        padrs = request.form['padrs']
        pcity = request.form['pcity']
        p_pin = request.form['p_pin']
        tadrs = request.form['tadrs']
        tcity = request.form['tcity']
        t_pin = request.form['t_pin']
        dob = request.form['dob']
        c_no = request.form['c_no']
        email = request.form['email']
        gender = request.form['gender']
        dept = request.form['dept']
        deg = request.form['deg']
        blood_group = request.form['blood_group']
        edu_qua = request.form['edu_qua']
        #cert = request.files['cert']
        ani = request.form['ani']
        religion = request.form['religion']
        driving_linc = request.form['driving_linc']
        voter_id = request.form['voter_id']
        adhaar = request.form['adhaar']
        #photo = request.files['photo']
        material_status = request.form['material_status']
        #resume = request.files['resume']
        doj = request.form['doj']
        first_employee = employee.query.filter_by(eid = eid).first()
        first_employee.fname = fname
        first_employee.lname = lname
        first_employee.father_name = father_name
        first_employee.padrs = padrs
        first_employee.pcity = pcity
        first_employee.p_pin = p_pin
        first_employee.tadrs = tadrs
        first_employee.tcity = tcity
        first_employee.t_pin = t_pin
        first_employee.dob = dob
        first_employee.c_no = c_no
        first_employee.email = email
        first_employee.gender = gender
        first_employee.dept = dept
        first_employee.deg = deg
        first_employee.blood_group = blood_group
        first_employee.edu_qua = edu_qua
        #first_employee.cert = cert
        first_employee.ani = ani
        first_employee.religion = religion
        first_employee.driving_linc = driving_linc
        first_employee.voter_id = voter_id
        first_employee.adhaar = adhaar
        first_employee.material_status = material_status
        #first_employee.photo = photo
        #first_employee.resume = resume
        first_employee.doj = doj
        db.session.add(first_employee)
        db.session.commit()
        flash("Successfully Updated the Employee",category='success')
        return render_template('updateEmployee.html',emp=None)
    else:
        eid = request.args.get("eid")
        find_employee = employee.query.filter_by(eid = eid).first()
        return render_template('updateEmployee.html',emp = find_employee)

@app.route("/searchEmployee",methods=["POST","GET"])
def searchEmployee():
    eid = request.args.get("eid")
    if eid == None:
        flash("No Employee's EID entered",category='danger')
    find_employee = employee.query.filter_by(eid = eid).first()
    if find_employee == None:
        flash("No Employee Found",category='danger')
    else:
        flash("Employee found",category='success')
    return render_template('searchEmployee.html',emp = find_employee)

@app.route("/deleteEmployee",methods=["POST","GET"])
def deleteEmployee():
    if request.method == "POST":
        eid = request.form['eid']
        emp = employee.query.filter_by(eid = eid).first()
        ex_emp = ex_employee(emp.eid, emp.fname, emp.lname, emp.father_name, emp.padrs, emp.pcity, emp.p_pin,
         emp.tadrs, emp.tcity, emp.t_pin, emp.dob, emp.c_no, emp.email, emp.gender, emp.dept, emp.deg, emp.blood_group,
          emp.edu_qua, emp.cert, emp.ani, emp.religion, emp.driving_linc, emp.voter_id, emp.adhaar, emp.material_status,
           emp.photo, emp.resume, emp.doj)
        employee.query.filter_by(eid = eid).delete()
        db.session.add(ex_emp)
        db.session.commit()
        flash("Successfully Terimated the employee",category="success")
        return render_template('deleteEmployee.html',emp="None")
    else:
        eid = request.args.get("eid")
        if eid == None:
            flash("No Employee's EID entered",category='danger')
        find_employee = employee.query.filter_by(eid = eid).first()
        if find_employee == None:
            flash("No Employee Found",category='danger')
        else:
            flash("Employee found",category='success')
        return render_template('deleteEmployee.html',emp = find_employee)

@app.route("/viewEmployees",methods=["POST","GET"])
def viewEmployees():
    return render_template('viewEmployees.html', employees = employee.query.filter_by().all())

@app.route("/attendance",methods=["POST","GET"])
def attendance():
    if request.method ==  "GET":
        eid = request.args.get("eid")
        dt = request.args.get("dt")
        find_employee = employee.query.filter_by(eid = eid).first()
        if eid == None:
            flash("No Employee's EID entered",category='danger')
        else:
            if find_employee == None:
                flash("No Employee Found",category='danger')
            else:
                flash("Employee Found",category='success')
        print(dt)
        return render_template('attendance.html',emp = find_employee)
    return render_template('attendance.html', emp = employee.query.filter_by().first())

@app.route("/logout")
def logout(): 
    session.pop('patient',None)
    session.pop('user',None)
    return redirect(url_for('login'))

@app.route("/copytodb")
def copytodb():
    try:
        emp = employee.query.filter_by(uid = 1).first()
        ex_emp = ex_employee(emp.eid, emp.fname, emp.lname, emp.father_name, emp.padrs, emp.pcity, emp.p_pin,
         emp.tadrs, emp.tcity, emp.t_pin, emp.dob, emp.c_no, emp.email, emp.gender, emp.dept, emp.deg, emp.blood_group,
          emp.edu_qua, emp.cert, emp.ani, emp.religion, emp.driving_linc, emp.voter_id, emp.adhaar, emp.material_status,
           emp.photo, emp.resume, emp.doj)
        db.session.add(ex_emp)
        db.session.commit()
        return f"WORKED"
    except:
        return f"didnot work"

@app.route("/downloadResume",methods=["POST","GET"])
def downloadResume():
    if request.method == "GET":
        eid = request.args.get("eid")
        find_employee = employee.query.filter_by(eid = eid).first()
        return send_file(BytesIO(find_employee.resume),attachment_filename="resume",as_attachment=True)
    return f"Well u have reached the downloaad resume page.<br> For better functionality u shouldnt visit here."
#######################################################################################

if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:5000/')
    db.create_all()
    app.run()