from models import db, User
from app import app


User.query.delete()


stevie = User(first_name = 'Stevie', last_name = 'Smith', image_url = 'static/cat1.jpeg')
rocky = User(first_name = 'Rock', last_name = 'Stone', image_url = 'static/dog1.jpeg')
flower = User(first_name = 'Folsom', last_name = 'Lady', image_url = 'static/cat2.jpeg')
monkey = User(first_name = 'Monkey', last_name = 'Guy', image_url = 'static/dog2.jpeg')

db.session.add_all([stevie, rocky, flower, monkey])
db.session.commit()

