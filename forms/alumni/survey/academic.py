from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import (
    StringField,
    FloatField,
    IntegerField,
    SelectField,
    TextAreaField,
    SubmitField,
)


class AcademicForm(FlaskForm):
    form_title = "Academic"
    route = "/academic"
    major = StringField(render_kw={"disabled": True})
    gpa = FloatField("GPA", render_kw={"disabled": True})
    graduation_year = IntegerField(render_kw={"disabled": True})
    postgraduate = SelectField(
        "Did you complete your postgraduate studies?",
        choices=[(0, "Select"), (1, "Yes"), (2, "No")],
        coerce=int,
    )
    postgrad_reason = TextAreaField(
        "What reasons prevented/helped you complete your postgraduate studies?",
        validators=[DataRequired()],
    )
    save = SubmitField()
