from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField
from wtforms.widgets import PasswordInput
from wtforms.validators import InputRequired, Length
from config import DEBUG


class LoginForm(FlaskForm):
    form_title = 'Login As:'

    route = "/login"
    
    role = RadioField(
        choices=[("Alumni"), ("Admin")], default="Alumni", validators=[InputRequired()]
    )

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=50)],
        render_kw={"placeholder": "Enter your username", "autofocus": "true"},
    )

    password = StringField(
        "Password",
        validators=[InputRequired(), Length(min=1, max=100)],
        render_kw={"placeholder": "Enter your password", "id": "password"},
        widget=PasswordInput(hide_value=False),
    ) if DEBUG else PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=1, max=100)],
        render_kw={"placeholder": "Enter your password", "id": "password"},
    )

    show_password = BooleanField(
        "Show Password",
        description="<span>Show Password</span>",
        render_kw={
            "onclick": "if(password.type=='text')password.type='password';else password.type='text';",
            "id": "eye",
        },
    )

    submit = SubmitField("Login", render_kw={"class": "submit"})
