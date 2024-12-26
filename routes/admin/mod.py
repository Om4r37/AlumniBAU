from flask import Blueprint, render_template
from utils import admin_required, mod_permission_required

bp = Blueprint("mod", __name__)


@bp.route("/mod")
@mod_permission_required
def mod():
    return render_template("admin/mod.jinja")
