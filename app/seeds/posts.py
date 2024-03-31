from app.models import db, Post, environment, SCHEMA
from sqlalchemy.sql import text
import datetime


def seed_posts():
    post1 = Post(
        content='I love this app!', user_id=1)
    post2 = Post(
        content='I hate this app!', user_id=2)
    post3 = Post(
        content='I am okay with this app!', user_id=3)

    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.commit()

def undo_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))
        
    db.session.commit()