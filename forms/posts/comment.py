from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField

class CommentForm(FlaskForm):
    route = "/comment"
    content = TextAreaField("Write a Comment:")
    submit = SubmitField("Post")