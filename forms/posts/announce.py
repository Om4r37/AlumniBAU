import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_tui_editor import TUIEditorField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed


options = {"hideModeSwitch": True, "height": "600px"}


class AnnounceForm(FlaskForm):
    route = "/announce"
    params = 'enctype="multipart/form-data"'
    title = StringField("Enter Title:", validators=[InputRequired()])
    file = FileField(
        "Add Thumbnail",
        render_kw={
            "accept": ".jpg, .jpeg, .png",
            "onchange": "loadFile(event)",
        },
        validators=[
            FileAllowed(["jpg", "png", "jpeg"], "Images only!"),
        ],
    )
    content = TUIEditorField("", render_kw={"editor_options": json.dumps(options)})
    submit = SubmitField("Post")
