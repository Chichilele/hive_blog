from app import app
from flask import render_template, request, flash, url_for
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "G"}
    posts = [
        {"author": {"username": "Magic E"}, "body": "Gig review!"},
        {"author": {"username": "HM Anibal Michael"}, "body": "Release day!"},
    ]
    return render_template("index.html", title=request.endpoint, user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login requested for user: {form.username.data}, remember_me={form.remember_me.data}"
        )
        return url_for("index")
    return render_template("login.html", title="Sign In", form=form)
