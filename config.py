import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    ## FLASK general
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY") or "you-will-never-guess-my-default"

    ## SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
