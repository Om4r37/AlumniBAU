from flask import Blueprint, redirect, render_template, session
from utils import login_required

bp = Blueprint("index", __name__)


@bp.route("/")
@login_required
def index():
    return redirect(
        "/survey"
        if session.get("role") == "alumnus"
        else (
            "/stats"
            if "stats" in session.get("perms")
            else (
                "/manage"
                if "manage" in session.get("perms")
                else (
                    "/announce"
                    if "announce" in session.get("perms")
                    else "/mod" if "mod" in session.get("perms") else "/news"
                )
            )
        )
    )


@bp.route("/about")
def about():
    return render_template("about.jinja")


@bp.route("/jobs")
def jobs():
    return render_template("jobs.jinja")
