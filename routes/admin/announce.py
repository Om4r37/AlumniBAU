from flask import Blueprint, render_template
from utils import announcer_required

bp = Blueprint("announce", __name__)


@bp.route("/announce")
@announcer_required
def announce():
    return render_template("admin/announce.jinja")
