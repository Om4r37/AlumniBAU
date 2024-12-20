from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


class UploadAlumniForm(FlaskForm):
    form_title = "Upload Alumni"
    params = 'enctype="multipart/form-data"'
    route = "/upload"
    file = FileField(
        validators=[
            FileRequired(message="Please select a file to upload"),
            FileAllowed(["csv"], "CSV files only!"),
        ],
        render_kw={"accept": ".csv"},
    )
    submit = SubmitField("Upload")
