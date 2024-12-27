from flask import Blueprint, render_template, session
from database.repo.repo import Repo

bp = Blueprint("news", __name__)


@bp.route("/news")
def news():
    posts = Repo.get_news()
    return render_template(
        "alumni/news.jinja",
        add=session.get("role") == "admin" and "announce" in session.get("perms"),
        posts=posts,
    )
