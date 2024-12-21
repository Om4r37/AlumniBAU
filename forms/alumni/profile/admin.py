from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField

class AdminProfileForm(FlaskForm):
    form_title = 'Admin Profile'
    route = "/profile"
    display_name = StringField(
        "Display Name",
        render_kw={"placeholder": "Enter your display_name", "autofocus": "true"},
    )
    
    picture = FileField(
        "Profile Picture",
        validators=[FileAllowed(["jpg", "png", "jpeg"], "Images only!"), FileRequired()],
    )
    
    submit = SubmitField("Update", render_kw={"class": "submit"})