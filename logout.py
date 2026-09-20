from flask import Flask, render_template, request,app

app = Flask(__name__)

@app.route('/logout')

def logout():
    name=''
    id=''
    msg = 'You have been logged out!'
    return render_template('login.html', msg=msg, name=name, id=id)