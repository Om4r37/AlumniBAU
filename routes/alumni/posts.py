from flask import Blueprint, render_template, redirect, session
from utils import login_required

bp = Blueprint("posts", __name__)


@bp.route("/posts")
@login_required
def posts():
    return render_template(
        "alumni/posts.jinja",
        add=(
            '<a href="/mod" class="btn btn-primary">Add Post</a>'
            if session.get("role") == "admin" and "mod" in session.get("perms")
            else ""
        ),
    )
