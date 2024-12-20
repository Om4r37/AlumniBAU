from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, IntegerField, SubmitField


class PersonalForm(FlaskForm):
    form_title = "Personal"
    route = "/personal"
    full_name = StringField(render_kw={"disabled": True})
    phone_number = IntegerField()
    email = EmailField()
    home_address = StringField()
    marital_status = SelectField(
        choices=[
            (1, "Select"),
            (2, "Single"),
            (3, "Married"),
            (4, "Divorced"),
            (5, "Widowed"),
        ],
        coerce=int,
    )
    save = SubmitField()
