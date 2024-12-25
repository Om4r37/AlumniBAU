import base64
from flask import Blueprint, flash, redirect, render_template, request, session
from database.repo import repo
from utils import login_required
from forms.profile.pfp import PFPForm
from forms.profile.alumni import EditAlumniProfileForm
from forms.profile.admin import EditAdminProfileForm


bp = Blueprint("profile", __name__)


@bp.route("/profile", methods=["GET", "POST"])
def profile():
    id = request.args.get("id")
    if id:
        id = int(id)
    else:
        id = session.get("id")

    if session.get("role") == "admin" and "stats" in session.get("perms"):
        fields = repo.get_alumnus_full_profile(id)
        fields.update({"pfp": base64.b64encode(repo.get_pfp(id)).decode()})
    elif session.get("id") == id and request.args.get("edit") == "1":
        data = dict(repo.get_alumnus_by_id(id))
        data.update(dict(repo.get_user(id)))
        form = EditAlumniProfileForm(data=data)
        form.pfp.description = f'<div class="container"><img src="data:image/png;base64,{base64.b64encode(repo.get_pfp(id)).decode()}" class="image"><a href="/pfp" class="middle text">Change</a></div>'
        if form.validate_on_submit():
            repo.edit_alumni_profile(form.data, id)
            flash("Profile updated successfully", "success")
        return render_template("alumni/profile/edit.jinja", form=form)
    elif session.get("id") == id:
        fields = repo.get_alumnus_public_profile(id)
        fields.update(
            {"pfp": base64.b64encode(repo.get_pfp(id)).decode(), "edit": True}
        )
    else:
        fields = {}
        data = repo.get_alumnus_public_profile(id)
        fields.update(data)
        fields.update({"pfp": base64.b64encode(repo.get_pfp(id)).decode()})
    return render_template("alumni/profile/public.jinja", fields=fields)


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
