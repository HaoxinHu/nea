from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        f = open("login.txt", "w")
        f.write(request.form.get('username') + ":" + request.form.get('pw'))
        f.close()
    return render_template('signup.html')

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?",
        (request.form['username'], request.form['password']))
        result = cur.fetchone()
        if result:
            return "Access granted"
        else:
            return "Access denied"
    return render_template('index.html')