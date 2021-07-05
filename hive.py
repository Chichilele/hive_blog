from typing import Dict
from app import flask_app, db
from app.models import User, Post


@flask_app.shell_context_processor
def make_shell_context() -> Dict:
    return {"db": db, "User": User, "Post": Post}
