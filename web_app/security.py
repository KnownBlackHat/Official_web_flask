import hashlib
import json
from flask import Flask,render_template,request

DATA_FILE="./web_app/data.json"

def hash(password):
    password_bytes = password.encode("utf-8")
    salt_bytes = "test_salt".encode("utf-8")
    return hashlib.sha256(salt_bytes+password_bytes).hexdigest()

def authenticate(email,password):
    with open(DATA_FILE,'r') as file:
        data = json.load(file)
    if data.get(email) and data[email]["password"]==password:
        return render_template('login.html',title="Log In", logact = "active", login=True)
    else:
        return render_template('login.html',title="Log In", logact = "active", login=False)

