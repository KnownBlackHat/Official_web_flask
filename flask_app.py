import json
from textwrap import indent
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", title="4FARMY" , indact = "active")


@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Us", conact = "active")

@app.route('/login', methods= ["GET", "POST"] )
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        with open('data.json','r') as file:
            data = json.load(file)
        data[email]={}
        data[email]["password"] = password
        json.dump(data,open('data.json','w'),indent=2)
    return render_template('login.html', title="Log In", logact = "active")

@app.route('/signup')
def signup():
    return render_template('signup.html', title="Sign Up", sigact = "active")
    
    
@app.route('/join')
def join():
    return render_template('join.html', title="Join Us", joiact = "active")
    
if __name__=="__main__":
    app.run(debug=True,port=80)