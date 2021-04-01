from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class EnterAppForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('enter the app')


class CreateRoomForm(FlaskForm):
    name = StringField('What do you want to call the chat room?', validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('Create Room')