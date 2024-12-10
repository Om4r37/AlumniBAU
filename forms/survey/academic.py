from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import (
    StringField,
    FloatField,
    IntegerField,
    BooleanField,
    TextAreaField,
    SubmitField,
)


class AcademicForm(FlaskForm):
    form_title = "Academic"

    route = "/academic"

    major = StringField(
        render_kw={"disabled": True},
    )

    gpa = FloatField(
        "GPA",
        render_kw={"disabled": True},
    )

    graduation_year = IntegerField(
        render_kw={"disabled": True},
    )

    postgrad = BooleanField(
        description="Did you complete your postgraduate studies?",
    )

    postgrad_reason = TextAreaField(
        "What reasons prevented/helped you complete your postgraduate studies?",
    )

    save = SubmitField()
