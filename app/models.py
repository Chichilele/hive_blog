from datetime import datetime
from app import db
from app import login

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    posts = db.relationship("Post", backref="author", lazy="dynamic")

    def __repr__(self) -> str:
        return f"<User='{self.username}', id='{self.id}'>"

    def set_password(self, password: str) -> None:
        """Hash and set user's password.

        Args:
            password (str): plain password
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Check user password against hash.

        Args:
            password (str): plain password to be tested.

        Returns:
            bool: True if password matches, false otherwise.
        """
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self) -> str:
        return f"<Post='{self.body}'>"


@login.user_loader
def load_user(id: int) -> User:
    """User loader for flask_login.

    Args:
        id (int): User primary id.

    Returns:
        User: User instance.
    """
    return User.query.get(id)
