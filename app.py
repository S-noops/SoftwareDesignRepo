from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
username = ""
logged_in = False

#MADE BY WAHEED NADEEM 2027898
@app.route('/')
def index():
    global username, logged_in
    username = ""
    logged_in = False
    try:
        return render_template('login_register.html', data=request.args.get('v'))
    except:
        return render_template('login_register.html', data="d")


@app.route('/login_check', methods=['POST'])
def checkLogin():
    global username, logged_in
    uname = request.form['uname']
    pswd = request.form['password']

    conn = sqlite3.connect("users.db")
    q1 = "select username, password from users where username = '{un}' and password = '{ps}'".format(
        un=uname, ps=pswd)
    rows = conn.execute(q1)
    rows = rows.fetchall()
    conn.close()
    if (len(rows) == 1):
        username = uname
        logged_in = True
        return redirect(url_for('home'))
    else:
        # return render_template('login_register.html', login_error=True, signup_error=False, signup_success=False)
        return redirect(url_for('index', v="a"))


@app.route('/signup_check', methods=['POST'])
def checkSignup():
    global username, logged_in
    uname = request.form['uname']
    pswd = request.form['password']
    email = request.form['email']

    conn = sqlite3.connect("users.db")
    q1 = "select username, password, email from users where username = '{un}' and password = '{ps}' and email = '{em}'".format(
        un=uname, ps=pswd, em=email)
    rows = conn.execute(q1)
    rows = rows.fetchall()
    if (len(rows) == 1):
        # return render_template('login_register.html', login_error=False, signup_error=True, signup_success=False)
        return redirect(url_for('index', v="b"))
    else:
        q2 = "insert into users (username, password, email) values('{un}','{ps}','{em}')".format(
            un=uname, ps=pswd, em=email)
        conn.execute(q2)
        conn.commit()
        conn.close()
        # return render_template('login_register.html', login_error=False, signup_error=False, signup_success=True)
        return redirect(url_for('index', v="c"))

#MADE BY Sanjay Paudel ID: 1908201

@app.route('/home')
def home():
    global logged_in,username
    if (logged_in==True):
        return render_template('index.html', user=username)
    else:
        return "<h1>Login To view content!</h1>"

@app.route('/fuel', methods=['GET', 'POST'])
def fuel():
    global logged_in,username
    if request.method == 'GET':
    
        conn = sqlite3.connect("users.db")
        q3 = "select add1, add2 from users where username='{un}'".format(un=username)
        row = conn.execute(q3)
        row = row.fetchone()
        conn.close()
        add = ""
        if (row!=None):
            if (row[0]==None):
                row[0] = "" 
            if (row[1]==None):
                row[1] = ""
            add = row[0] + row[1] 
        if (logged_in==True):
            return render_template('fuelQoute.html',  user=username, address =add, success= False)
        else:
            return "<h1>Login To view content!</h1>"
    else:
        conn = sqlite3.connect("users.db")
        gallons= request.form['gallonreq']
        date= str(request.form['deldate'])
        sugamt = request.form['sugprice']
        total = request.form['dueamount']
        address = request.form['deladdress']
        q5 = "insert into history values ('{g}','{a}','{d}','{s}','{t}','{u}')".format(g=gallons,a=address,d=date,s=sugamt,t=total,u=username)
        conn.execute(q5)
        conn.commit()
        conn.close()
        return render_template('fuelQoute.html',  user=username, address =address, success= True)


# MADE BY: ADRIAN RODRIGUEZ-MARTINEZ ID: 2036096
@app.route('/fuelhis')
def fuelhis():
    global logged_in,username
    conn = sqlite3.connect("users.db")
    q6 = "select * from history where username = '{un}'".format(un=username)
    rows =conn.execute(q6)
    rows = rows.fetchall()
    conn.close()
    if (logged_in==True):
        return render_template('fuelQouteHistory.html',  user=username, data=rows)
    else:
        return "<h1>Login To view content!</h1>"

@app.route('/user', methods=['GET', 'POST'])
def user():
    global logged_in,username
    if request.method == 'GET':
        conn = sqlite3.connect("users.db")
        q3 = "select * from users where username='{un}'".format(un=username)
        row = conn.execute(q3)
        row = row.fetchone()
        conn.close()
        values=[]
        if (row!=None):
            for i in row:
                if (i==None):
                    values.append("")
                else:
                    values.append(i)
        if (logged_in==True):
            return render_template('userProfile.html', user=username, name=values[3], add1=values[4], add2=values[5], city=values[6], state=values[7], zipcode=values[8],success=False)
        else:
            return "<h1>Login To view content!</h1>"
    else:
        conn = sqlite3.connect("users.db")
        name = request.form['name']
        add1 = request.form['add1']
        add2 = request.form['add2']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zipcode']
        q4 = "update users set name='{n}', add1='{a1}', add2='{a2}', city='{c}', state='{s}', zipcode='{z}'".format(n=name,a1=add1,a2=add2,c=city,s=state,z=zipcode)
        conn.execute(q4)
        conn.commit()
        conn.close()
        return render_template('userProfile.html', user=username, name=name, add1=add1, add2=add2, city=city, state=state, zipcode=zipcode,success=True)


if __name__ == '__main__':
    app.run(debug=True)
