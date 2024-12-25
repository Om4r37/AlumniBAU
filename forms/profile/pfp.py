from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


class PFPForm(FlaskForm):
    form_title = "Change Profile Picture"
    route = "/pfp"
    params = 'enctype="multipart/form-data"'
    file = FileField(
        "Change Photo",
        render_kw={
            "accept": ".jpg, .jpeg, .png",
            "onchange": "loadFile(event)",
        },
        validators=[
            FileRequired(),
            FileAllowed(["jpg", "png", "jpeg"], "Images only!"),
        ],
    )
    submit = SubmitField("Save")
