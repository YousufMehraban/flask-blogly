
from flask import Flask, redirect, render_template, request
from models import db, User

app = Flask(__name__)
app.config['SECRET KEY'] = 'nothing so secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True




db.app = app
db.init_app(app)
# db.drop_all()
# db.create_all()

@app.route('/')
def show_users():
    """display list of all the users in the database"""

    users = User.query.all()
    return render_template('users.html', users = users)


@app.route('/add_user')
def show_user_form():
    """show the add new user form"""

    return render_template('add_user.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    """adding a new user to the app"""

    first = request.form.get('first_name')
    last = request.form.get('last_name')
    image = request.form.get('image_url')

    new_user = User(first_name = first, last_name = last, image_url = image)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')

@app.route('/<user_id>')
def show_user_detials(user_id):
    """displaying detials of a user"""

    user = User.query.get_or_404(user_id)
    return render_template('user_detail.html', user=user)

@app.route('/edit_user/<user_id>')
def show_edit_form(user_id):
    """displaying edit form of a user"""

    user = User.query.get_or_404(user_id)
    return render_template('edit_user.html', user = user, user_id=user_id)

@app.route('/edit_user/<user_id>', methods=['POST'])
def edit_user(user_id):
    """editing a user information"""

    user = User.query.get_or_404(user_id)

    user.first_name = request.form.get('first_name')
    user.last_name = request.form.get('last_name')
    user.image_url = request.form.get('image_url')

    db.session.add(user)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<user_id>')
def delete_user(user_id):
    """deleting a user from the database"""

    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect('/')
