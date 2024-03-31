from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, DateField
from wtforms.validators import DataRequired, Email, ValidationError
from app.api.aws_helpers import ALLOWED_EXTENSIONS
from app.models import User

    
class EditUserForm(FlaskForm):
    handle = StringField('handle')
    profile_picture = FileField('profile_picture', validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])
    banner_picture = FileField('banner_picture', validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])
    bio = StringField('bio')
    birth_date = DateField('birth_date', format='%Y-%m-%d', validators=[DataRequired()])
    location = StringField('location')
    website = StringField('website')