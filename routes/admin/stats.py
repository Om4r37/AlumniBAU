from flask import Blueprint, render_template
from utils import data_access_required
from database.repo.admin import Admin
from database.repo.alumnus import Alumnus


bp = Blueprint("stats", __name__)


@bp.route("/stats")
@data_access_required
def stats():
    stats = Admin.get_stats()
    return render_template("admin/stats/stats.jinja", stats=stats)


@bp.route("/alumni")
@data_access_required
def alumni():
    alumni = Alumnus.get_all_alumni()
    return render_template("admin/stats/alumni.jinja", alumni=alumni)
