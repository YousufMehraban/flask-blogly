from models import db, User, Post
from app import app


db.drop_all()
db.create_all()


stevie = User(first_name = 'Stevie', last_name = 'Smith', image_url = 'static/cat1.jpeg')
rocky = User(first_name = 'Rock', last_name = 'Stone', image_url = 'static/dog1.jpeg')
flower = User(first_name = 'Folsom', last_name = 'Lady', image_url = 'static/cat2.jpeg')
monkey = User(first_name = 'Monkey', last_name = 'Guy', image_url = 'static/dog2.jpeg')

db.session.add_all([stevie, rocky, flower, monkey])
db.session.commit()

funny = Post(title = 'Hahaha', content = 'a chicken crossed the road', created_at = '2022-1-1 05:33.55', user_id = 1)
OMG = Post(title = 'oh my god', content = 'he had an accident', created_at = '2022-1-3 07:33.55', user_id = 2)
sad = Post(title = 'Sad', content = 'he is got fired', created_at = '2022-1-2 02:33.55', user_id = 1)

db.session.add_all([funny, OMG, sad])
db.session.commit()

