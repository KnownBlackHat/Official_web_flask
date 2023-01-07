import hashlib
import json
from threading import Thread
from flask import Flask,render_template,request

app=Flask(__name__)


# TODO: Replace following function in another file
def hash(password):
    password_bytes = password.encode("utf-8")
    salt_bytes = "test_salt".encode("utf-8")
    return hashlib.sha256(salt_bytes+password_bytes).hexdigest()

def authenticate(email,password):
    with open('data.json','r') as file:
        data = json.load(file)
    if data.get(email) and data[email]["email"]==email and data[email]["password"]==password:
        return render_template('login.html',title="Log In", logact = "active", login=True)
    else:
        return render_template('login.html',title="Log In", logact = "active", login=False)



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
        password = hash(request.form.get('password'))
        return authenticate(email,password)
    else:
        return render_template('login.html', title="Log In", logact = "active")

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        with open('data.json','r') as file:
            data = json.load(file)
        name = request.form.get('Name')
        email = request.form.get('Email')
        if data.get(email):
            return render_template('signup.html', title="Sign Up", logact = "active",account_exist=True)
        password = hash(request.form.get('Password'))
        data[email]={}
        data[email]["email"]=email
        data[email]["name"]=name
        data[email]["password"]=password
        with open('data.json','w') as file:
            json.dump(data,file)
        
        return render_template('login.html', title="home", logact = "active",login=True)
    else:    
        return render_template('signup.html', title="Sign Up", sigact = "active")


@app.route('/join')
def join():
    return render_template('join.html', title="Join Us", joiact = "active")



def run():
    app.run(host="0.0.0.0", port=80)

def keep_alive():
    server = Thread(target=run)
    server.start()
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=80)
