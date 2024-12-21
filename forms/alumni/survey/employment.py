from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    TextAreaField,
    StringField,
    DateField,
    IntegerField,
    SubmitField,
)


class EmploymentForm(FlaskForm):
    form_title = "Employment"
    route = "/employment"
    does_work = SelectField(
        "Are you currently working?",
        choices=[(0, "Select"), (1, "Yes"), (2, "No")],
        coerce=int,
        render_kw={"onchange": "employment()"},
    )
    reason = TextAreaField("What reasons prevented you from working?")
    sector = SelectField(
        "Work Sector",
        choices=[(0, "Select"), (1, "Public"), (2, "Private")],
        coerce=int,
    )
    place = StringField("Company Name")
    address = StringField("Company Address")
    date = DateField("Date of Employment", format="%Y-%m-%d")
    title = StringField("Job Title")
    phone = IntegerField("Company Phone Number")
    save = SubmitField()
