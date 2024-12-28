from flask import Blueprint, render_template, session, request
from utils import login_required
from database.repo.repo import Repo

bp = Blueprint("posts", __name__)


@bp.route("/posts")
@login_required
def posts():
    return render_template(
        "alumni/posts.jinja",
        add=session.get("role") == "admin" and "mod" in session.get("perms"),
    )


@bp.route("/post")
def post():
    id = request.args.get("id")
    if id:
        return render_template(
            "other/post.jinja",
            post=Repo.get_post(id),
        )