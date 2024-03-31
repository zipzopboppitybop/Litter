from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, DateField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from app.api.aws_helpers import ALLOWED_EXTENSIONS
from app.models import User


class PostForm(FlaskForm):
    content = StringField('content')
    file_one = FileField('file_one', validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])
    file_two = FileField('file_two', validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])
    file_three = FileField('file_three', validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])
    file_four = FileField('file_four', validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])
    user_id = IntegerField('owner')