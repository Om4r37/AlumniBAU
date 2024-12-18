from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField


class EditAdminForm(FlaskForm):
    form_title = "Edit Admin"
    route = "/edit"
    manage = BooleanField("Is Manager", description="<span>Is Manager</span>")
    announce = BooleanField("Can Announce", description="<span>Can Announce</span>")
    stats = BooleanField("Has Data Access", description="<span>Has Data Access</span>")
    mod = BooleanField("Is Moderator", description="<span>Is Moderator</span>")
    submit = SubmitField("Save", render_kw={"class": "submit"})
