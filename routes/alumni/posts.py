from flask import Blueprint, render_template, redirect, flash, session, request
from utils import login_required
from database.repo.repo import Repo
from database.repo.user import User
from forms.posts.post import PostForm
from forms.posts.comment import CommentForm

bp = Blueprint("posts", __name__)


@bp.route("/post")
@login_required
def post():
    id = request.args.get("id")
    if not id:
        return redirect("/posts")
    form = CommentForm()
    return render_template(
        'alumni/posts/post.jinja',
        post=Repo.get_post(id),
        comments=Repo.get_comments(id),
        form=form,
    )


@bp.route("/posts")
@login_required
def posts():
    return render_template(
        "alumni/posts/posts.jinja",
        posts=User.get_posts(),
    )


@bp.route("/announcement")
def announce():
    id = request.args.get("id")
    if not id:
        return redirect("/news")
    form = CommentForm()
    form.route = "/comment?id=" + id
    return render_template(
        f'{"admin/posts" if session.get("role") == "admin" and "announce" in session.get("perms") else "alumni/posts" if session.get("id") else "other"}/post.jinja',
        post=Repo.get_news_post(id),
        comments=Repo.get_comments(id),
        form=form,
    )


@bp.route("/write_post", methods=["GET", "POST"])
@login_required
def write_post():
    form = PostForm()
    if form.validate_on_submit():
        User.create_post(form.data, session.get("id"))
        flash("Announcement created successfully!", "success")
        return redirect("/posts")
    return render_template("alumni/posts/write_post.jinja", form=form)


@bp.route("/comment", methods=["POST"])
@login_required
def comment():
    id = request.args.get("id")
    form = CommentForm()
    if form.validate_on_submit():
        User.create_comment(form.data, session.get("id"), id)
        flash("Comment posted successfully!", "success")
    return redirect(f"/announcement?id={id}")
