from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

DB_NAME = 'database.db'

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
        (request.form.get('username'), request.form.get('pw')))
        con.commit()
        con.close()
    return render_template('signup.html')

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?",
        (request.form['username'], request.form['pw']))
        result = cur.fetchone()
        con.close()
        if result:
            return "Access granted"
        else:
            return "Access denied"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)