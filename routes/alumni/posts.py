from flask import Blueprint, render_template, redirect, flash, session, request
from utils import login_required
from database.repo.repo import Repo
from database.repo.user import User
from forms.posts.post import PostForm

bp = Blueprint("posts", __name__)


@bp.route("/posts")
@login_required
def posts():
    return render_template(
        "alumni/posts/posts.jinja",
        posts=Repo.get_posts(),
    )


@bp.route("/announcement")
def announce():
    id = request.args.get("id")
    if id:
        return render_template(
            f'{"admin/posts" if session.get("role") == "admin" and "announce" in session.get("perms") else "other"}/post.jinja',
            post=Repo.get_news_post(id),
        )


@bp.route("/post", methods=["GET", "POST"])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        User.create_post(form.data, session.get("id"))
        flash("Announcement created successfully!", "success")
        return redirect("/posts")
    return render_template("alumni/posts/post.jinja", form=form)