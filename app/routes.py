from typing import Union

from flask import flash, redirect, render_template, request, url_for
from flask.wrappers import Response

from app import flask_app
from app.forms import LoginForm


@flask_app.route("/")
@flask_app.route("/index")
def index() -> str:
    user = {"username": "G"}
    posts = [
        {"author": {"username": "Magic E"}, "body": "Gig review!"},
        {"author": {"username": "HM Anibal Michael"}, "body": "Release day!"},
    ]
    return render_template("index.html", title=request.endpoint, user=user, posts=posts)


@flask_app.route("/login", methods=["GET", "POST"])
def login() -> Union[str, Response]:
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login requested for user: {form.username.data}, remember_me={form.remember_me.data}"
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)