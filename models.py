
from flask_sqlalchemy import SQLAlchemy

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