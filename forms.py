from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ChatGPTForm(FlaskForm):
    user_input = TextAreaField('Your question or message:', validators=[DataRequired()])
    submit = SubmitField('Send')
