from flask import Blueprint, flash, redirect, render_template, request, session
from utils import manager_required
from forms.manage.upload_alumni import UploadAlumniForm
from forms.manage.hash_file import hashFileForm
from forms.manage.add_admin import AddAdminForm
from forms.manage.edit_admin import EditAdminForm
from database.repo.admin import Admin

bp = Blueprint("manage", __name__)


@bp.route("/manage")
@manager_required
def manage():
    return render_template("admin/manage/manage.jinja")


@bp.route("/upload", methods=["GET", "POST"])
@manager_required
def upload():
    form = UploadAlumniForm()
    if form.validate_on_submit():
        count = Admin.add_alumni(form.file.data)
        flash(f"Successfully added {count} alumni")
    return render_template("admin/manage/upload.jinja", form=form)


@bp.route("/hash", methods=["GET", "POST"])
@manager_required
def hash():
    form = hashFileForm()
    if form.validate_on_submit():
        Admin.hash_file(form.file_name.data)
        flash(f"Successfully hashed {form.file_name.data}")
    return render_template("admin/manage/hash.jinja", form=form)


@bp.route("/admins")
@manager_required
def admins():
    admins = Admin.get_all_admins(session.get("id"))
    return render_template("admin/manage/admins.jinja", admins=admins)


@bp.route("/add", methods=["GET", "POST"])
@manager_required
def add():
    form = AddAdminForm()
    if form.validate_on_submit():
        Admin.add_admin(form.data)
        flash(f"Successfully added {form.username.data}")
    return render_template("admin/manage/add.jinja", form=form)


@bp.route("/edit", methods=["GET", "POST"])
@manager_required
def edit():
    id = request.args.get("id")
    admin = Admin.get_admin_by_id(id)
    form = EditAdminForm(data=admin, id=id)
    form.form_title = "Edit Admin: " + admin["username"]
    if form.validate_on_submit():
        Admin.edit_admin(form.data, id)
        flash(f"Successfully edited {admin["username"]}")
    return render_template("admin/manage/admin.jinja", form=form)


@bp.route("/delete")
@manager_required
def delete():
    id = request.args.get("id")
    name = Admin.delete_admin(id)
    flash(f"Successfully deleted {name}")
    return redirect("/admins")
