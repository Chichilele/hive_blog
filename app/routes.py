from typing import Tuple, Union

from flask import flash, redirect, render_template, request, url_for
from werkzeug.urls import url_parse
from flask.wrappers import Response
from flask_login import current_user, login_user, login_required, logout_user

from app import flask_app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User


@flask_app.route("/")
@flask_app.route("/index")
@login_required
def index() -> str:
    """Index view.

    Returns:
        str: rendered index.html template
    """
    posts = [
        {"author": {"username": "Magic E"}, "body": "Gig review!"},
        {"author": {"username": "HM Anibal Michael"}, "body": "Release day!"},
    ]
    return render_template("index.html", title=request.endpoint, posts=posts)


@flask_app.route("/login", methods=["GET", "POST"])
def login() -> Union[str, Response]:
    """Login view. Logs in the user or returns the index view if already logged in.

    Returns:
        Union[str, Response]: index view if logged in, login view otherwise.
    """
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()

    ## POST request
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    ## GET request
    else:
        return render_template("login.html", title="Sign In", form=form)


@flask_app.route("/logout")
def logout() -> Response:
    """Logout view. Logs out the user and redirects to index.

    Returns:
        Response: redirection to index.
    """
    logout_user()
    return redirect(url_for("index"))


@flask_app.route("/register", methods=["GET", "POST"])
def register() -> Union[Response, str]:
    """Register view. Registers the user and redirects to login.

    Returns:
        Union[Response, str]: [description]
    """
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    ## POST
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash("Congratulations, you are now a registered user!")

        return redirect(url_for("login"))
    ## GET
    else:
        return render_template("register.html", title="Register", form=form)
