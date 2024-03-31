from flask import Blueprint, jsonify, request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, db
from app.forms import SignUpForm, EditUserForm
from app.api.aws_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()

@user_routes.route('/<int:id>/edit', methods=['PUT'])
@login_required
def edit_user(id):
    """
    Query for a user by id and edit that user in a dictionary
    """
    user = User.query.get(id)

    if user is None:
        return {"errors": "User not found"}, 404
    
    if current_user.id != user.id:
        return {"errors": "Unauthorized"}, 401
    
    form = EditUserForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():

        if form.data['profile_picture']:
            if user.profile_picture:
                remove_file_from_s3(user.profile_picture)
            profile_image = form.data['profile_picture']
            profile_image_upload = upload_file_to_s3(profile_image)

            if "url" not in profile_image_upload:
                return {"errors": "Url not in upload_image"}, 400
            
            url = profile_image_upload["url"]
            user.profile_picture = url
            db.session.commit()
        
        if form.data['banner_picture']:
            if user.banner_picture:
                remove_file_from_s3(user.banner_picture)
            banner_image = form.data['banner_picture']
            banner_image_upload = upload_file_to_s3(banner_image)

            if "url" not in banner_image_upload:
                return {"errors": "Url not in upload_image"}, 400
            
            url = banner_image_upload["url"]
            user.banner_picture = url
            db.session.commit()

        user.bio = form.data['bio']
        user.birth_date = form.data['birth_date']
        user.location = form.data['location']
        user.website = form.data['website']
        db.session.commit()
        return user.to_dict()
    
    return {"errors": form.errors}, 400

