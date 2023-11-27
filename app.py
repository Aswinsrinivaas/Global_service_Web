import os
import mysql.connector
import mysql.connector as mysql
from flask import Flask, render_template, request, flash, redirect, url_for, session
from mysql.connector import connection, cursor
from flask_mysqldb import MySQL
from logging import FileHandler, WARNING

app = Flask(__name__)

app.secret_key = os.urandom(24)
app.secret_key = "ayush"


@app.route('/')
def home():  # put application's code here
    return render_template('index.html')


@app.route("/Login")
def Login():
    return render_template("login.html")


@app.route("/adminhome")
def adminhome():
    return render_template("adminhome.html")


@app.route("/dhome")
def dhome():
    return render_template("donorhome.html")


@app.route("/userhome")
def userhome():
    return render_template("userhome.html")


@app.route("/Register")
def Register():
    return render_template("register.html")


@app.route("/addapproval")
def addapproval():
    return render_template("Approval.html")


@app.route("/donation")
def donation():
    return render_template("adddonor.html")


@app.route("/addfund")
def addfund():
    db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                  database='medical_service')

    if 'name' in session:
        email = session['name']
    if 'uname' in session:
        name = session['uname']


    else:
        print("Not in sesson")
    cursor = db_connection.cursor()
    cursor.execute("select MAX(id) from fund")
    data = cursor.fetchone()
    lid = data[0]
    if lid == None:
        lid = "1"
    else:
        lid = lid + 1

    return render_template("addfund.html", lid=lid, sid=email, sid1=name)


@app.route("/donorRegister")
def donorRegister():
    return render_template("donorregister.html")


@app.route('/checklogin', methods=['POST'])
def checklogin(rows=None):
    if request.method == 'POST' and 'name' in request.form and 'pass' in request.form:
        username = request.form['name']
        password = request.form['pass']
        usertype = request.form['utype']
    if username == "Admin" and password == "Admin" and usertype == "Admin":
        flash("Login Success")
        return render_template('hospital.html')

    if usertype == "User":
        db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                      database='medical_service')
        cursor = db_connection.cursor()
        cursor.execute("SELECT username,password,name FROM registration WHERE username = '%s' AND password = '%s' "
                       % (username, password))
        account = cursor.fetchone()
        uname, password, user_name = account

        if account:
            flash("Login Success")
            print("welcome")
            session['name'] = request.form['name']
            session['uname'] = user_name

        return render_template('userhome.html')

    if usertype == "Donor":
        db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                      database='medical_service')

        cursor = db_connection.cursor()
        cursor.execute("SELECT username,password FROM donorregistration WHERE username = '%s' AND password = '%s' "
                       % (username, password))
        account = cursor.fetchone()
        if account:
            flash("Login Success")

        return render_template('donorhome.html')


@app.route('/checkhospital', methods=['POST'])
def checkhospital():
    if request.method == 'POST':
        usertype = request.form['utype']
        print("WELCOME")
        db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                      database='medical_service')
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM fund WHERE hname = '%s'  "
                       % (usertype))
        data = cursor.fetchall()
        cursor.close()
        return render_template('viewdonreg.html', userlist=data)


@app.route('/register_details', methods=['POST'])
def register_details():
    if request.method == "POST":
        uname = request.form['name']
        email = request.form['Email']
        contact = request.form['contact']
        address = request.form['Address']
        username = request.form['Username']
        password = request.form['Password']

        db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                      database='medical_service')
        cursor = db_connection.cursor()

        cursor.execute(
            "INSERT INTO registration (name,Email,contact,Address,username,password ) VALUES(%s, %s, %s,%s, %s, %s)",
            (uname, email, contact, address, username, password))
        db_connection.commit()

        return render_template('Login.html')


@app.route('/donor_details', methods=['POST'])
def donor_details():
    if request.method == "POST":
        uname = request.form['name']
        email = request.form['Email']
        contact = request.form['contact']
        address = request.form['Address']
        username = request.form['Username']
        password = request.form['Password']

        db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                      database='medical_service')
        cursor = db_connection.cursor()

        cursor.execute(
            "INSERT INTO donorregistration (name,Email,contact,Address,username,password ) VALUES(%s, %s, %s,%s, %s, %s)",
            (uname, email, contact, address, username, password))
        db_connection.commit()

        return render_template('Login.html')


@app.route('/fund_details', methods=['POST'])
def fund_details():
    if request.method == "POST":
        Requestid = request.form['id']
        Name = request.form['name']
        FundAmount = request.form['amt']
        Regid = request.form['regid']
        Disease = request.form['disease']
        HospitalName = request.form['utype1']
        Priority = request.form['utype']
        f = request.files['proof']
        f.save("static/uploads/" + f.filename)
        f1 = request.files['proof2']
        f1.save("static/uploads/" + f1.filename)

        UPI = request.form['upi']
        status = "pending"
        db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                      database='medical_service')
        cursor = db_connection.cursor()

        cursor.execute(
            "INSERT INTO fund (id,name,amt,regid,disease,hname,Priority,proof,proof2,upi,statusinfo ) VALUES(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s)",
            (Requestid, Name, FundAmount, Regid, Disease, HospitalName, Priority, f.filename, f1.filename,
             UPI, status))

        db_connection.commit()

        return render_template('index.html')


@app.route('/approval', methods=['POST'])
def approval():
    if request.method == "POST":
        Requestid = request.form['id']
        status = request.form['tid5a']
        db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                      database='medical_service')
        cursor = db_connection.cursor()
        statement = "UPDATE fund SET statusinfo='" + status + "'  WHERE id ='" + Requestid + "'"

        cursor.execute(statement)

        db_connection.commit()

        return render_template('index.html')


@app.route('/donor', methods=['POST'])
def donor():
    if request.method == "POST":
        Requestid = request.form['id']

        getinfo = request.form['getinfo1']
        pname = request.form['pname']
        Amount = request.form['amt']
        payusername = request.form['puname']

        upid = request.form['upid']
        Remarks = request.form['remarks']
        name = 'admin'
        # if len(getinfo) >= 0:

        print("welcome" + pname)

        if getinfo.__eq__("uploaddonation"):

            if (len(pname) > 1):
                f = request.files['pproof']
                f.save("static/uploads1/" + f.filename)
                db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                              database='medical_service')
                cursor = db_connection.cursor()

                cursor.execute(
                    "INSERT INTO donor (id,pname,amt,puname,file,upid,remarks ) VALUES(%s, %s, %s,%s, %s,%s,%s)",
                    (Requestid, pname, Amount, payusername, f.filename, upid, Remarks))

                db_connection.commit()
                return render_template('index.html')
            if len(pname) <= 1:
                db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                              database='medical_service')
                cursor = db_connection.cursor()

                cursor.execute("SELECT id,name,upi FROM fund WHERE id = '%s' OR name = '%s'  "
                               % (Requestid, name))
                account = cursor.fetchone()

                idinfo, nameinfo, upiinfo = account

                return render_template('adddonor.html', glid=Requestid, gname=nameinfo, gupi=upiinfo)


@app.route('/Viewuser')
def Viewuser():
    db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                  database='medical_service')
    cursor = db_connection.cursor()
    cursor.execute("SELECT  * from registration")
    data = cursor.fetchall()
    cursor.close()
    return render_template('viewuser.html', userlist=data)


@app.route('/viewfund')
def viewfund():
    db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                  database='medical_service')
    cursor = db_connection.cursor()
    cursor.execute("SELECT  * from fund")
    data = cursor.fetchall()
    cursor.close()
    return render_template('viewfund.html', fundlist=data)


@app.route('/viewfund1')
def viewfund1():
    db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                  database='medical_service')
    cursor = db_connection.cursor()
    cursor.execute("SELECT  * from fund where statusinfo='Approved' ")
    data = cursor.fetchall()
    cursor.close()
    return render_template('viewfund1.html', fundlist=data)


@app.route('/viewfund2')
def viewfund2():
    db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                  database='medical_service')
    cursor = db_connection.cursor()
    cursor.execute("SELECT  * from fund where statusinfo='Approved' ")
    data = cursor.fetchall()
    cursor.close()
    return render_template('viewfund2.html', fundlist=data)


@app.route('/viewfund3')
def viewfund3():
    if 'uname' in session:
        name = session['uname']
    print("user fund view"+name)
    db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                  database='medical_service')
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM fund WHERE name = '%s' "
                   % (name))
    data = cursor.fetchall()
    cursor.close()
    return render_template('viewfund3.html', fundlist=data)


@app.route('/viewapproval')
def viewapproval():
    db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                  database='medical_service')
    cursor = db_connection.cursor()
    cursor.execute("SELECT  id,statusinfo from fund where statusinfo='Approved'")
    data = cursor.fetchall()
    cursor.close()
    return render_template('viewapproval.html', approvallist=data)


@app.route('/viewapproval1')
def viewapproval1():
    if request.method == 'POST':
        statusinfo = "Approved"

        db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                      database='medical_service')
        cursor = db_connection.cursor()
        cursor.execute("SELECT id,statusinfo FROM fund WHERE statusinfo = '%s'  "
                       % (statusinfo))
        data = cursor.fetchall()
        cursor.close()
        return render_template('viewapproval1.html', approvallist=data)


@app.route('/viewdonor')
def viewdonor():
    db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                  database='medical_service')
    cursor = db_connection.cursor()
    cursor.execute("SELECT  * from donor")
    data = cursor.fetchall()
    cursor.close()
    return render_template('viewdonor.html', donorlist=data)


@app.route('/viewdonor1')
def viewdonor1():
    if 'uname' in session:
        name = session['uname']
    print("user" + name)
    db_connection = mysql.connect(user='root', password='root', host='127.0.0.1', charset='utf8',
                                  database='medical_service')
    cursor = db_connection.cursor()

    cursor.execute("SELECT  * from donor  WHERE pname = '%s' " % (name))
    data = cursor.fetchall()
    cursor.close()
    return render_template('viewdonor1.html', donorlist=data)


if __name__ == '__main__':
    app.run()
