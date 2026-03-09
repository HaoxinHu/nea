from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pw = request.form.get('pw')
        if pw == "password":
            return "Access granted"
        else:   
            return "Access denied"
    return render_template('index.html')