import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_tui_editor import TUIEditorField
from wtforms.validators import InputRequired

options = {"hideModeSwitch": True, "height": "600px"}


class PostForm(FlaskForm):
    route = "/post"
    title = StringField("Enter Title:", validators=[InputRequired()])
    content = TUIEditorField("", render_kw={"editor_options": json.dumps(options)})
    submit = SubmitField("Post")
