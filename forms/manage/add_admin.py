from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, EqualTo


class AddAdminForm(FlaskForm):
    form_title = "Add Admin"

    route = "/add"

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=50)],
        render_kw={"placeholder": "Enter your username", "autofocus": "true"},
    )

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

    manage = BooleanField("Is Manager", description="<span>Is Manager</span>")
    announce = BooleanField("Can Announce", description="<span>Can Announce</span>")
    stats = BooleanField("Has Data Access", description="<span>Has Data Access</span>")
    mod = BooleanField("Is Moderator", description="<span>Is Moderator</span>")

    submit = SubmitField("Add", render_kw={"class": "submit"})
