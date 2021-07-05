from app import app
from flask import render_template, request


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "G"}
    posts = [
        {"author": {"username": "Magic E"}, "body": "Gig review!"},
        {"author": {"username": "HM Anibal Michael"}, "body": "Release day!"},
    ]
    return render_template("index.html", title=request.endpoint, user=user, posts=posts)
