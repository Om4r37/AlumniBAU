from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField


class EditAdminForm(FlaskForm):
    def __init__(self, id, *args, **kwargs):
        super(EditAdminForm, self).__init__(*args, **kwargs)
        self.id = id
        self.route = f"/edit_admin?id={id}"
        self.delete = f"/delete?id={id}"

    form_title = "Edit Admin"
    manage = BooleanField("Is Manager", description="<span>Is Manager</span>")
    announce = BooleanField("Can Announce", description="<span>Can Announce</span>")
    stats = BooleanField("Has Data Access", description="<span>Has Data Access</span>")
    mod = BooleanField("Is Moderator", description="<span>Is Moderator</span>")
    submit = SubmitField("Save", render_kw={"class": "submit"})
