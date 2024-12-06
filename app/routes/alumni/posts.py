from flask import Blueprint, render_template, redirect, session
from app.utils import login_required

bp = Blueprint("posts", __name__)


@bp.route("/posts")
@login_required
def posts():
    return (
        redirect("/mod")
        if session["id"] == 1
        else render_template("alumni/posts.jinja")
    )
