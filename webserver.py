import json
from threading import Thread
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
        print(email ,password)
        with open('data.json','r') as file:
            data = json.load(file)
        try:
            if email == data[email] and password == data[password]:
                print("correct")
                return "<script>alert('logged in succesfully')</script>"
            # else:
            #     print("wrong")
            #     return "<script>alert('Wrong id or password')</script>"
        # data[email]={}
        # data[email]["password"] = password
        # json.dump(data,open('data.json','w'),indent=2)
        except KeyError:
                print("wrong")
                return "<script>alert('Wrong id or password')</script>" 
                
    return render_template('login.html', title="Log In", logact = "active")
@app.route('/signup')
def signup():
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
