from re import sub
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired(), Length(min=1, max=50)]
    )
    password = PasswordField(
        "Password", validators=[InputRequired(), Length(min=1, max=100)]
    )

    submit = SubmitField("Login")
