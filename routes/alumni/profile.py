import base64
from flask import Blueprint, redirect, render_template, request, session
from database.repo import repo
from utils import login_required
from forms.alumni.profile.private import PrivateProfileForm
from forms.alumni.profile.public import PublicProfileForm
from forms.alumni.profile.admin_public import AdminProfileForm
from forms.alumni.profile.pfp import PFPForm

bp = Blueprint("profile", __name__)


@bp.route("/profile")
@login_required
def profile():
    id = request.args.get("id")
    if not id:
        id = session.get("id")
    if session.get("role") == "admin" and "stats" in session.get("perms"):
        form = AdminProfileForm(data=repo.get_alumnus_by_id(id))
        form.elements[0] = (
            f'<img src="data:image/png;base64,{base64.b64encode(repo.get_pfp(id)).decode()}"/>'
        )
    elif session.get("id") == id:
        form = PrivateProfileForm(data=repo.get_alumnus_by_id(id))
        form.elements[0] = (
            f'<div class="container"><img src="data:image/png;base64,{base64.b64encode(repo.get_pfp(id)).decode()}" class="image"><a href="/pfp" class="middle text">Change Photo</a></div>'
        )
    else:
        form = PublicProfileForm(data=repo.get_alumnus_by_id(id))
        form.elements[0] = (
            f'<img src="data:image/png;base64,{base64.b64encode(repo.get_pfp(id)).decode()}"/>'
        )
    return render_template("alumni/profile/profile.jinja", form=form)


@bp.route("/pfp", methods=["GET", "POST"])
@login_required
def pfp():
    id = session.get("id")
    pfp = {"profile_picture": repo.get_pfp(id)}
    form = PFPForm(data=pfp)
    if form.validate_on_submit():
        repo.update_pfp(id, form.file.data)
        return redirect("/pfp")
    form.file.label = f'<img id="output" src="data:image/png;base64,{base64.b64encode(pfp.get('profile_picture')).decode()}"/>'
    return render_template("alumni/profile/pfp.jinja", form=form)
