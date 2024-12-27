from flask import Blueprint, render_template, session
from database.repo import repo

bp = Blueprint("news", __name__)


@bp.route("/news")
def news():
    posts = repo.get_news()
    return render_template(
        "alumni/news.jinja",
        add=session.get("role") == "admin" and "announce" in session.get("perms"),
        posts=posts,
    )
