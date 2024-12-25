import base64
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class PrivateProfileForm(FlaskForm):
    form_title = "Your Profile"
    route = "/profile"
    elements = []
    elements.append('<img src="/static/pics/pfp.png">')
    elements.append('<a href="/change_password">Change Password</a>')

    display_name = StringField(
        "Display Name",
        render_kw={"placeholder": "Enter your display name", "autofocus": "true"},
    )
    submit = SubmitField("Update", render_kw={"class": "submit"})
