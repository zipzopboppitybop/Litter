from .db import db, environment, SCHEMA, add_prefix_for_prod


class Post(db.Model):
    __tablename__ = "posts"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(130), nullable=True)
    file_one = db.Column(db.String)
    file_two = db.Column(db.String)
    file_three = db.Column(db.String)
    file_four = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('users.id')), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())

    owner = db.relationship('User', back_populates='posts')

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'userId': self.userId,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'owner_name': self.owner.username,
            'owner_handle': self.owner.handle,
            'owner_profile_picture': self.owner.profile_picture,
            'owner_banner_picture': self.owner.banner_picture,
            'owner_bio': self.owner.bio,
            'owner_id': self.owner.id,
        }