from flask import Blueprint, redirect, render_template

bp = Blueprint("index", __name__)


@bp.route("/")
def index():
    return redirect("/news")


@bp.route("/about")
def about():
    return render_template("other/about.jinja")


@bp.route("/jobs")
def jobs():
    return render_template("other/jobs.jinja")
