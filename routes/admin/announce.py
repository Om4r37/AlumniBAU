import base64
from flask import Blueprint, flash, redirect, render_template, session, request
from utils import announcer_required
from forms.posts.announce import AnnounceForm
from forms.posts.edit_announcements import EditAnnouncementForm
from forms.posts.edit_thumbnail import EditThumbnailForm
from database.repo.admin import Admin
from database.repo.repo import Repo

bp = Blueprint("announce", __name__)


@bp.route("/announce", methods=["GET", "POST"])
@announcer_required
def announce():
    form = AnnounceForm()
    if form.validate_on_submit():
        Admin.create_announcement(form.data, session.get("id"))
        flash("Announcement created successfully!", "success")
        return redirect("/news")
    return render_template("admin/news/announce.jinja", form=form)


@bp.route("/edit_announcement", methods=["GET", "POST"])
@announcer_required
def edit():
    id = request.args.get("id")
    announcement = Repo.get_news_post(id)
    form = EditAnnouncementForm(data=announcement, id=id)
    form.route = f"/edit_announcement?id={id}"
    form.file.label = f'<div class="container"><img src="data:image/png;base64,{base64.b64encode(announcement.get("thumbnail")).decode()}" class="image"><a href="/edit_thumbnail?id={id}" class="middle green">Change</a></div>'
    if form.validate_on_submit():
        Admin.edit_announcement(form.data, id)
        flash("Announcement edited successfully!", "success")
        return redirect("/news")
    return render_template("admin/news/edit.jinja", form=form)


@bp.route("/edit_thumbnail", methods=["GET", "POST"])
@announcer_required
def edit_thumbnail():
    id = request.args.get("id")
    announcement = Repo.get_news_post(id)
    form = EditThumbnailForm(data=announcement, id=id)
    form.file.label = f'<img id="output" src="data:image/png;base64,{base64.b64encode(Repo.get_thumbnail(id)).decode()}"/>'
    form.route = f"/edit_thumbnail?id={id}"
    if form.validate_on_submit():
        Admin.edit_thumbnail(form.data, id)
        flash("Thumbnail edited successfully!", "success")
        return redirect("/edit_thumbnail?id=" + id)
    return render_template("admin/news/edit_thumbnail.jinja", form=form, id=id)