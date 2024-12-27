from flask import Blueprint, render_template, session
from utils import login_required

bp = Blueprint("posts", __name__)


@bp.route("/posts")
@login_required
def posts():
    return render_template(
        "alumni/posts.jinja",
        add=session.get("role") == "admin" and "mod" in session.get("perms"),
    )
