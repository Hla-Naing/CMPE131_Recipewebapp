

from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime
import pytz

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    recipes = db.relationship('Recipe', backref='author', lazy=True)

# To use your timezone
def get_local_time():
    tz = pytz.timezone('America/Los_Angeles')  
    return datetime.now(tz)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=True)  
    instructions = db.Column(db.Text, nullable=True)
    image_filename = db.Column(db.String(120), nullable=True)
    created = db.Column(db.DateTime, default=get_local_time)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)    
    rating_sum = db.Column(db.Integer, default=0)
    rating_count = db.Column(db.Integer, default=0)
    user = db.relationship('User', backref=db.backref('user_recipes', lazy=True))

    @property
    def average_rating(self):
        if not self.rating_count or not self.rating_sum:
            return None
        return round(self.rating_sum / self.rating_count, 1)


#Users have individual displays profiles tied to their account, which are optional
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    bio = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    
