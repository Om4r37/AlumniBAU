from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class EditAdminProfileForm(FlaskForm):
    form_title = "Edit Profile"
    route = "/edit_profile"
    pfp = StringField(label="", render_kw={"class": "pfp", "type": "hidden"})
    display_name = StringField(
        "Display Name",
        render_kw={"placeholder": "Enter your display_name", "autofocus": "true"},
        validators=[InputRequired()],
        description='<a href="/change_password" class="centered text">Change Password</a>',
    )
    submit = SubmitField("Update", render_kw={"class": "submit"})
