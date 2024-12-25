from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class AdminProfileForm(FlaskForm):
    form_title = 'Admin Profile'
    route = "/profile"
    display_name = StringField(
        "Display Name",
        render_kw={"placeholder": "Enter your display_name", "autofocus": "true"},
    )

    submit = SubmitField("Update", render_kw={"class": "submit"})