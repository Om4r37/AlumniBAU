from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField
from wtforms.validators import InputRequired


class RecoverAccountForm(FlaskForm):
    form_title = "Recover Account"
    route = "/recover_account"
    email = EmailField(
        "Email",
        validators=[InputRequired()],
        render_kw={"placeholder": "Enter your email", "autofocus": "true"},
    )
    submit = SubmitField(render_kw={"class": "submit"})
