from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import InputRequired


class EditAlumniProfileForm(FlaskForm):
    form_title = "Your Profile"
    route = "/profile?edit=1"
    pfp = StringField(label='', render_kw={"class": "pfp", "type": "hidden"})
    display_name = StringField(
        "Display Name",
        render_kw={"placeholder": "Enter your display name", "autofocus": "true"},
        validators=[InputRequired()],
        description='<a href="/change_password" class="centered text">Change Password</a>'
    )
    personal_privacy = RadioField(
        description="Personal Information Privacy:",
        choices=[("Public"), ("Private")],
        default="Public",
        validators=[InputRequired()],
        render_kw={"class": "radio"},
    )
    academic_privacy = RadioField(
        description="Academic Information Privacy:",
        choices=[("Public"), ("Private")],
        default="Public",
        validators=[InputRequired()],
        render_kw={"class": "radio"},
    )
    employment_privacy = RadioField(
        description="Employment Information Privacy:",
        choices=[("Public"), ("Private")],
        default="Public",
        validators=[InputRequired()],
        render_kw={"class": "radio"},
    )
    # employment = employment.EmploymentForm()
    submit = SubmitField("Update", render_kw={"class": "submit"})
