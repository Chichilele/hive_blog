from hive import flask_app, db
from hive.models import User, Post


@flask_app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}
