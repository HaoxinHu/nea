from flask import Flask, render_template, request

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
        pw = request.form['password']
        f = open("login.txt", "r")
        stored_data = f.read().split(":")
        f.close()
        if request.form.get('username') == stored_data[0] and request.form.get('pw') == stored_data[1]:
            return "Logged in!"
    return render_template('index.html')