import base64
from flask import Blueprint, redirect, render_template, request, session
from utils import login_required
from forms.alumni.profile.private import PrivateProfileForm
from forms.alumni.profile.public import PublicProfileForm
from forms.alumni.profile.admin import AdminProfileForm
from forms.alumni.profile.pfp import PFPForm
from database.repo import repo

bp = Blueprint("profile", __name__)


@bp.route("/profile")
@login_required
def profile():
    id = request.args.get("id")
    if not id:
        id = session.get("id")
    form = (
        AdminProfileForm
        if session.get("role") == "admin" and "stats" in session.get("perms")
        else PrivateProfileForm if session.get("id") == id else PublicProfileForm
    )(data=repo.get_alumnus_by_id(id))
    return render_template("alumni/profile/profile.jinja", form=form)


@bp.route("/pfp", methods=["GET", "POST"])
@login_required
def pfp():
    id = session.get("id")
    pfp = dict(repo.get_pfp(id))
    form = PFPForm(data=pfp)
    form.file.label = f'<img id="output" src="data:image/png;base64,{base64.b64encode(pfp.get('profile_picture')).decode()}"/>'
    if form.validate_on_submit():
        repo.update_pfp(id, form.file.data)
        form.file.label = f'<img id="output" src="data:image/png;base64,{base64.b64encode(pfp.get('profile_picture')).decode()}"/>'
        return redirect("/pfp")
    return render_template("alumni/profile/pfp.jinja", form=form)