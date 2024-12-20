from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import SelectField, TextAreaField, SubmitField


class FeedbackForm(FlaskForm):
    form_title = "Feedback"
    route = "/feedback"
    does_communicate = SelectField(
        "Do you communicate with the university?",
        choices=[(0, "Select"), (1, "Yes"), (2, "No")],
        coerce=int,
    )
    does_follow = SelectField(
        "Do you follow university activities and events?",
        choices=[(0, "Select"), (1, "Yes"), (2, "No")],
        coerce=int,
    )
    supports_club = SelectField(
        "Do you support creating an alumni club?",
        choices=[(0, "Select"), (1, "Yes"), (2, "No")],
        coerce=int,
    )
    suggestion = TextAreaField(
        "Do you have any suggestions?", validators=[InputRequired()]
    )
    save = SubmitField()
