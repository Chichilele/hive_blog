from app import app
from flask import render_template, request


@app.route("/")
def home():
    user = {"username": "G"}
    return render_template("index.html", title=request.endpoint, user=user)


@app.route("/index")
def index():
    user = {"username": "G"}
    return render_template("index.html", title=request.endpoint, user=user)
