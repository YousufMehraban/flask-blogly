
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()

# def connect_db(app):
#     db.app = app
#     db.init_app(app)

class User(db.Model):
    """creating a user info table"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement = True, primary_key= True)
    first_name = db.Column(db.String(30), nullable = False, unique = True)
    last_name = db.Column(db.String(30), nullable = False)
    image_url = db.Column(db.Text, nullable= True, default = None)


    def __repr__(self):
        return f'<User id={self.id}, first={self.first_name}, last={self.last_name}>'

class Post(db.Model):
    """creating a Post Model"""

    __tablename__ = 'posts'

    id = db.Column(db.Integer, autoincrement = True, primary_key= True)
    title = db.Column(db.String(30), nullable = False, unique = True)
    content = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    users = db.relationship('User', backref='posts')


