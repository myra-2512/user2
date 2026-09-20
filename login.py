import mysql.connector
from flask import app, request
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in    request.form:
        username = request.form['username']
        password = request.form['password']
        mydb= mysql.connector.connect(
        host="remotemysql.com",
        user="Rz8hqnldk4",
        password="nd0wk03xe0",
        database="Rz8hqnldk4"
        )
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM LoginDetails WHERE username = %s AND password = %s', (username, password,))
        account = mycursor.fetchone()
        if account:
            print("login success")
            name=[1]
            id=account[0]
            msg="login succesful"
            print("login success")
            return render_template('index.html', msg=msg, name=name, id=id)
        else:
            msg = 'Incorrect username / password !'
            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html')
