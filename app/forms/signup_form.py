from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, DateField
from wtforms.validators import DataRequired, Email, ValidationError
from app.api.aws_helpers import ALLOWED_EXTENSIONS
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')


class SignUpForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(), username_exists])
    email = StringField('email', validators=[DataRequired(), user_exists])
    password = StringField('password', validators=[DataRequired()])
    handle = StringField('handle')
    profile_picture = FileField('profile_picture', validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])
    banner_picture = FileField('banner_picture', validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])
    bio = StringField('bio')
    birth_date = DateField('birth_date', format='%Y-%m-%d', validators=[DataRequired()])
    location = StringField('location')
    website = StringField('website')
