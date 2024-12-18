from flask import Blueprint, flash, redirect, render_template, request
from utils import admin_required, manager_required
from forms.manage.upload_alumni import UploadAlumniForm
from forms.manage.hash_file import hashFileForm
from forms.manage.add_admin import AddAdminForm
from forms.manage.edit_admin import EditAdminForm
from database.repo import repo

bp = Blueprint("manage", __name__)


@bp.route("/manage")
@admin_required
@manager_required
def manage():
    return render_template("admin/manage/manage.jinja")


@bp.route("/upload", methods=["GET", "POST"])
@admin_required
@manager_required
def upload():
    form = UploadAlumniForm()
    if form.validate_on_submit():
        count = repo.add_alumni(form.file.data)
        flash(f"Successfully added {count} alumni")
    return render_template("admin/manage/upload.jinja", form=form)


@bp.route("/hash", methods=["GET", "POST"])
@admin_required
@manager_required
def hash():
    form = hashFileForm()
    if form.validate_on_submit():
        repo.hash_file(form.file_name.data)
        flash(f"Successfully hashed {form.file_name.data}")
    return render_template("admin/manage/hash.jinja", form=form)


@bp.route("/admins")
@admin_required
@manager_required
def admins():
    admins = repo.get_all_admins()
    return render_template("admin/manage/admins.jinja", admins=admins)


@bp.route("/add", methods=["GET", "POST"])
@admin_required
@manager_required
def add():
    form = AddAdminForm()
    if form.validate_on_submit():
        repo.add_admin(form.data)
        flash(f"Successfully added {form.username.data}")
    return render_template("admin/manage/add.jinja", form=form)


@bp.route("/edit", methods=["GET", "POST"])
@admin_required
@manager_required
def edit():
    id = request.args.get("id")
    admin = repo.get_admin_by_id(id)
    form = EditAdminForm(data=admin, id=id)
    form.form_title = "Edit Admin: " + admin["username"]
    if form.validate_on_submit():
        repo.edit_admin(form.data, id)
        flash(f"Successfully edited {admin["username"]}")
    return render_template("admin/manage/admin.jinja", form=form)


@bp.route("/delete")
@admin_required
@manager_required
def delete():
    id = request.args.get("id")
    repo.delete_admin(id)
    flash("Successfully deleted admin")
    return redirect("/admins")