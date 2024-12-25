from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField

class PrivateProfileForm(FlaskForm):
    form_title = 'Your Profile'
    route = "/profile"
    file = FileField(
        label='<span>Change Image</span>',
        validators=[FileAllowed(["jpg", "png", "jpeg"], "Images only!")],
        render_kw={"onchange": "loadFile(event)"},
    )
    display_name = StringField(
        "Display Name",
        render_kw={"placeholder": "Enter your display_name", "autofocus": "true"},
    )
    submit = SubmitField("Update", render_kw={"class": "submit"})