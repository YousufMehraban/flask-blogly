"""Models for Blogly."""

from email.policy import default
from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()


class User(db.Model):
    """creating a user info table"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement = True, primary_key= True)
    first_name = db.Column(db.String(30), nullable = False, unique = True)
    last_name = db.Column(db.String(30), nullable = False)
    image_url = db.Column(db.Text, nullable= True, default = None)

    posts = db.relationship('Post', backref='users', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<User id={self.id}, first={self.first_name}, last={self.last_name}>'

class Post(db.Model):
    """creating a Post Model"""

    __tablename__ = 'posts'

    id = db.Column(db.Integer, autoincrement = True, primary_key= True)
    title = db.Column(db.String(30), nullable = False)
    content = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    def __repr__(self):
        return f'<Post id={self.id}, title={self.title}, content={self.content}>'



