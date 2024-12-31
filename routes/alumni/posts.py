from flask import Blueprint, render_template, session, request
from utils import login_required
from database.repo.repo import Repo

bp = Blueprint("posts", __name__)


@bp.route("/posts")
@login_required
def posts():
    return render_template(
        "alumni/posts/posts.jinja",
        posts=Repo.get_news(),
    )


@bp.route("/announcement")
def post():
    id = request.args.get("id")
    if id:
        return render_template(
            f'{"admin/posts" if session.get("role") == "admin" and "announce" in session.get("perms") else "other"}/post.jinja',
            post=Repo.get_news_post(id),
        )