import json
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, SubmitField
from flask_tui_editor import TUIEditorField
from wtforms.validators import InputRequired


options = {"hideModeSwitch": True, "height": "600px"}


class EditAnnouncementForm(FlaskForm):
    route = "/edit_announcement"
    params = 'enctype="multipart/form-data"'
    title = StringField("Enter Title:", validators=[InputRequired()])
    file = HiddenField()
    content = TUIEditorField("", render_kw={"editor_options": json.dumps(options)})
    submit = SubmitField("Save Changes")
