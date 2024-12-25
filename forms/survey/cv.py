from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


class CVForm(FlaskForm):
    form_title = "Curriculum Vitae"
    route = "/cv"
    params = 'enctype="multipart/form-data"'
    cv = FileField(
        "Upload CV",
        description="<a href='/cv' target='_blank'>Download your CV</a>",
        render_kw={"accept": ".pdf"},
        validators=[
            FileRequired(),
            FileAllowed(upload_set=["pdf"], message="PDF files only!"),
        ],
    )

    submit = SubmitField("Upload")
