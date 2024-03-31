from flask import Blueprint, jsonify, request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, db, Post
from app.forms import SignUpForm, EditUserForm, PostForm
from app.api.aws_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3
from app.api.auth_routes import validation_errors_to_error_messages

post_routes = Blueprint('posts', __name__)


@post_routes.route('/')
def posts():
    """
    Query for all posts and returns them in a list of post dictionaries
    """
    posts = Post.query.all()
    return {'posts': [post.to_dict() for post in posts]}


@post_routes.route('/<int:id>')
def post(id):
    """
    Query for a post by id and returns that post in a dictionary
    """
    post = Post.query.get(id)

    if post is None:
        return {"errors": "Post not found"}, 404

    return post.to_dict()


@post_routes.route('/create', methods=['POST'])
@login_required
def create_post():
    """
    Create a post
    """
    form = PostForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        post = Post(
            content=form.data['content'],
            user_id=current_user.id
        )

        db.session.add(post)
        db.session.commit()

        if form.data['file_one']:
            file_one = form.data['file_one']
            file_one_upload = upload_file_to_s3(file_one)

            if "url" not in file_one_upload:
                return {"errors": "Url not in upload_image"}, 400

            url = file_one_upload["url"]
            post.file_one = url
            db.session.commit()

        if form.data['file_two']:
            file_two = form.data['file_two']
            file_two_upload = upload_file_to_s3(file_two)

            if "url" not in file_two_upload:
                return {"errors": "Url not in upload_image"}, 400

            url = file_two_upload["url"]
            post.file_two = url
            db.session.commit()

        if form.data['file_three']:
            file_three = form.data['file_three']
            file_three_upload = upload_file_to_s3(file_three)

            if "url" not in file_three_upload:
                return {"errors": "Url not in upload_image"}, 400

            url = file_three_upload["url"]
            post.file_three = url
            db.session.commit()

        if form.data['file_four']:
            file_four = form.data['file_four']
            file_four_upload = upload_file_to_s3(file_four)

            if "url" not in file_four_upload:
                return {"errors": "Url not in upload_image"}, 400

            url = file_four_upload["url"]
            post.file_four = url
            db.session.commit()

        return post.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@post_routes.route('/<int:id>/edit', methods=['PUT'])
@login_required
def edit_post(id):
    """
    Edit a post
    """
    form = PostForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        post = Post.query.get(id)

        if post is None:
            return {"errors": "Post not found"}, 404
        
        if current_user.id != post.user_id:
            return {"errors": "Unauthorized"}, 401

        post.content = form.data['content']
        db.session.commit()

        if form.data['file_one']:
            if post.file_one:
                remove_file_from_s3(post.file_one)

            file_one = form.data['file_one']
            file_one_upload = upload_file_to_s3(file_one)

            if "url" not in file_one_upload:
                return {"errors": "Url not in upload_image"}, 400

            url = file_one_upload["url"]
            post.file_one = url
            db.session.commit()

        if form.data['file_two']:
            if post.file_two:
                remove_file_from_s3(post.file_two)

            file_two = form.data['file_two']
            file_two_upload = upload_file_to_s3(file_two)

            if "url" not in file_two_upload:
                return {"errors": "Url not in upload_image"}, 400

            url = file_two_upload["url"]
            post.file_two = url
            db.session.commit()

        if form.data['file_three']:
            if post.file_three:
                remove_file_from_s3(post.file_three)

            file_three = form.data['file_three']
            file_three_upload = upload_file_to_s3(file_three)

            if "url" not in file_three_upload:
                return {"errors": "Url not in upload_image"}, 400

            url = file_three_upload["url"]
            post.file_three = url
            db.session.commit()

        if form.data['file_four']:
            if post.file_four:
                remove_file_from_s3(post.file_four)

            file_four = form.data['file_four']
            file_four_upload = upload_file_to_s3(file_four)

            if "url" not in file_four_upload:
                return {"errors": "Url not in upload_image"}, 400

            url = file_four_upload["url"]
            post.file_four = url
            db.session.commit()

        return post.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@post_routes.route('/<int:id>/delete', methods=['DELETE'])
@login_required
def delete_post(id):
    """
    Delete a post
    """
    post = Post.query.get(id)

    if post is None:
        return {"errors": "Post not found"}, 404
    
    if current_user.id != post.user_id:
        return {"errors": "Unauthorized"}, 401

    if post.file_one:
        remove_file_from_s3(post.file_one)

    if post.file_two:
        remove_file_from_s3(post.file_two)

    if post.file_three:
        remove_file_from_s3(post.file_three)

    if post.file_four:
        remove_file_from_s3(post.file_four)

    db.session.delete(post)
    db.session.commit()

    return {'message': 'Post deleted'}