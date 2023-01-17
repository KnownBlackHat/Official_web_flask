import hashlib
import json
from threading import Thread
from flask import Flask,render_template,request
from security import hash,authenticate


app=Flask(__name__)
@app.route('/')

def index():
    return render_template("index.html", title="4FARMY" )


@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Us")


@app.route('/login', methods= ["GET", "POST"] )
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = hash(request.form.get('password'))
        return authenticate(email,password)
    else:
        return render_template('login.html', title="Log In")

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        with open('data.json','r') as file:
            data = json.load(file)
        name = request.form.get('Name')
        email = request.form.get('Email')
        if data.get(email):
            return render_template('signup.html', title="Sign Up",account_exist=True)
        password = hash(request.form.get('Password'))
        data[email]={}
        data[email]["email"]=email
        data[email]["name"]=name
        data[email]["password"]=password
        with open('data.json','w') as file:
            json.dump(data,file)
        
        return render_template('login.html', title="home",login=True)
    else:    
        return render_template('signup.html', title="Sign Up")


@app.route('/join')
def join():
    return render_template('join.html', title="Join Us")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=8080)
