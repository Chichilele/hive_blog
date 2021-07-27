from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired()])
    password2 = StringField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_username(self, username: str):
        """username custom validator.

        Args:
            username (str): form's username.

        Raises:
            ValidationError: username already taken.
        """
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username taken, please use a different one.")

    def validate_email(self, email: str):
        """email custom validator.

        Args:
            email (str): form's email address.

        Raises:
            ValidationError: Email address already taken.
        """
        user = User.query.filter_by(username=email.data).first()
        if user is not None:
            raise ValidationError("Email address taken, please use a different one.")
