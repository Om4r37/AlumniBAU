from flask import Blueprint, render_template, redirect, request, session, flash
from forms.auth.login import LoginForm
from forms.auth.change_password import ChangePasswordForm
from forms.auth.recover_account import RecoverAccountForm
from werkzeug.security import check_password_hash
from database.repo.admin import Admin
from database.repo.alumnus import Alumnus
from config import DEBUG, MAIL_USERNAME, MAIL_PASSWORD
import yagmail

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if DEBUG:
        session.clear()

    if session.get("id"):
        return redirect("/")

    form = LoginForm()

    if request.method == "GET":
        return render_template("auth/login.jinja", form=form)

    if not form.validate_on_submit():
        flash("Invalid credentials.", "danger")
        return render_template("auth/login.jinja", form=form)

    role = form.role.data
    username = form.username.data
    password = form.password.data
    rows = (Admin.get_admins if role == "Admin" else Alumnus.get_alumni)(username)
    if len(rows) and check_password_hash(rows[0]["password_hash"], password):
        session["id"] = rows[0]["id"]
        session["username"] = username
        session["role"] = "alumnus"
        if role == "Admin":
            session["role"] = "admin"
            session["perms"] = Admin.get_perms(username)
            name = username
        else:
            name = rows[0]["full_name"]
        flash("Logged in as " + name, "success")
        return redirect("/")

    flash("Invalid credentials.", "danger")
    return render_template("auth/login.jinja", form=form)


@bp.route("/change_password", methods=["GET", "POST"])
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        (
            Admin.update_password
            if session.get("role") == "admin"
            else Alumnus.update_password
        )(session.get("id"), form.password.data)
        flash("Password Changed Successfully!")
    return render_template("auth/change_password.jinja", form=form)


@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@bp.route("/recover_account", methods=["GET", "POST"])
def recover_account():
    form = RecoverAccountForm()
    if form.validate_on_submit():
        email = form.email.data
        if Alumnus.check_email(email):
            subject = "BAU Alumni Account Recovery"
            contents = "Your new password is: " + Alumnus.recover_account(email)
            yag = yagmail.SMTP(MAIL_USERNAME, MAIL_PASSWORD)
            yag.send(email, subject, contents)
            yag.close()
            flash("A new password was sent to your email", "success")
        else:
            flash("Email not found.", "danger")
    return render_template("auth/recover_account.jinja", form=form)
