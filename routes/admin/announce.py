from flask import Blueprint, render_template, session
from utils import announcer_required
from forms.posts.announce import AnnounceForm
from database.repo.admin import Admin

bp = Blueprint("announce", __name__)


@bp.route("/announce", methods=["GET", "POST"])
@announcer_required
def announce():
    form = AnnounceForm()
    if form.validate_on_submit():
        Admin.create_announcement(form.data, session.get("id"))
    return render_template("admin/announce.jinja", form=form)
