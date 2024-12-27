import base64
from flask import Blueprint, flash, redirect, render_template, request, session
from utils import login_required
from database.repo.user import User
from database.repo.alumnus import Alumnus
from database.repo.admin import Admin
from forms.profile.pfp import PFPForm
from forms.profile.alumni import EditAlumniProfileForm
from forms.profile.admin import EditAdminProfileForm


bp = Blueprint("profile", __name__)


@bp.route("/profile")
def profile():
    id = request.args.get("id")
    if id:
        id = int(id)
    else:
        return redirect(f"/profile?id={session.get('id')}")

    fields = User.get_user_public_profile(id)
    fields.update({"pfp": base64.b64encode(User.get_pfp(id)).decode()})
    if session.get("id") == id:
        fields.update({"edit": True})
    elif session.get("role") == "admin" and "stats" in session.get("perms"):
        fields.update(User.get_user_full_profile(id))
    return render_template("profile/public.jinja", fields=fields)


@bp.route("/pfp", methods=["GET", "POST"])
@login_required
def pfp():
    id = session.get("id")
    pfp = {"profile_picture": User.get_pfp(id)}
    form = PFPForm(data=pfp)
    if form.validate_on_submit():
        User.update_pfp(id, form.file.data)
        return redirect("/pfp")
    form.file.label = f'<img id="output" src="data:image/png;base64,{base64.b64encode(pfp.get('profile_picture')).decode()}"/>'
    return render_template("profile/pfp.jinja", form=form)


@bp.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    id = session.get("id")
    data = dict(User.get_user(id))
    if session.get("role") == "admin":
        data.update(dict(Admin.get_admin_by_id(id)))
        form = EditAdminProfileForm(data=data)
    else:
        data.update(dict(Alumnus.get_alumnus_by_id(id)))
        form = EditAlumniProfileForm(data=data)
    form.pfp.description = f'<div class="container"><img src="data:image/png;base64,{base64.b64encode(User.get_pfp(id)).decode()}" class="image"><a href="/pfp" class="middle text">Change</a></div>'
    if form.validate_on_submit():
        (
            Admin.edit_admin_profile(form.data, id)
            if session.get("role") == "admin"
            else Alumnus.edit_alumni_profile(form.data, id)
        )
        flash("Profile updated successfully", "success")
    return render_template(f"profile/edit.jinja", form=form)
