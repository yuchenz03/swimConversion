from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello World"

@app.route("/login")
def test():
    return render_template("login.html")

@app.route("/page1")
def page():
    return render_template("page1.html")