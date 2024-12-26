from flask import Blueprint, render_template, session

bp = Blueprint("news", __name__)


@bp.route("/news")
def news():
    return render_template(
        "alumni/news.jinja",
        add=(
            '<a href="/announce" class="btn btn-primary">Add Announcement</a>'
            if session.get("role") == "admin" and "announce" in session.get("perms")
            else ""
        ),
    )
