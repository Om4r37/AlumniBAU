import json
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_tui_editor import TUIEditorField

options = {"hideModeSwitch": True, "height": "600px"}


class PostForm(FlaskForm):
    route = "/post"
    content = TUIEditorField("", render_kw={"editor_options": json.dumps(options)})
    submit = SubmitField("Post")
