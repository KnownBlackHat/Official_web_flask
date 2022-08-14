from turtle import title
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", title="4FARMY" , indact = "active")


@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Us", conact = "active")

@app.route('/login')
def login():
    return render_template('login.html', title="Log In", logact = "active")

@app.route('/signin')
def signin():
    return render_template('signin.html', title="Sign In", sigact = "active")
    
    
@app.route('/join')
def join():
    return render_template('join.html', title="Join Us", joiact = "active")
    
if __name__=="__main__":
    app.run(debug=True,port=80)