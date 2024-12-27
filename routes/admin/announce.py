from flask import Blueprint, render_template, session
from utils import announcer_required
from forms.announce import AnnounceForm
from database.repo import repo

bp = Blueprint("announce", __name__)


@bp.route("/announce", methods=["GET", "POST"])
@announcer_required
def announce():
    form = AnnounceForm()
    if form.validate_on_submit():
        repo.create_announcement(form.data, session.get("id"))
    return render_template("admin/announce.jinja", form=form)
