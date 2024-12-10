from flask import Blueprint, render_template
from utils import admin_required, announcer_required

bp = Blueprint("announce", __name__)


@bp.route("/announce")
@admin_required
@announcer_required
def announce():
    return render_template("admin/announce.jinja")
