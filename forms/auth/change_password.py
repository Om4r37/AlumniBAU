from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, EqualTo


class ChangePasswordForm(FlaskForm):
    form_title = 'Change Password'
    route = "/change_password"
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=1, max=100)],
        render_kw={"placeholder": "Enter your password", "id": "password"},
    )
    confirm = PasswordField(
        "Confirm Password",
        validators=[EqualTo("password", message="Passwords must match")],
        render_kw={"placeholder": "Confirm your password", "id": "confirm"},
    )
    show_password = BooleanField(
        "Show Password",
        description="<span>Show Password</span>",
        render_kw={
            "onclick": "if(password.type=='text'){password.type='password';confirm.type='password';}else{password.type='text';confirm.type='text';}",
            "id": "eye",
        },
    )
    submit = SubmitField("Change", render_kw={"class": "submit"})
