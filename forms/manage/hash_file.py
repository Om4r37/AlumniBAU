from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class hashFileForm(FlaskForm):
    form_title = "Enter the absolute path:"
    route = "/hash"
    file_path = StringField(validators=[InputRequired()])
    submit = SubmitField("Submit")