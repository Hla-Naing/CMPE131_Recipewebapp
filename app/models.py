
# Import necessary modules and objects
from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime
import pytz


# Association table for favorites
favorites = db.Table('favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'))
)

# Association table for recipe-tag many-to-many
recipe_tags = db.Table('recipe_tags',
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

# Callback function for Flask-Login to load a user by ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User model representing registered users
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Unique user ID
    username = db.Column(db.String(20), unique=True, nullable=False)  # Username
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email address
    password = db.Column(db.String(60), nullable=False)  # Hashed password
    recipes = db.relationship('Recipe', backref='author', lazy=True, overlaps="user,user_recipes")
    profile = db.relationship('Profile', backref='user', uselist=False)  # Relationship to profile (one-to-one)
    favorites = db.relationship(
        'Recipe',
        secondary=favorites,
        backref=db.backref('favorited_by', lazy='dynamic'),
        lazy='dynamic'
    )

# Helper function to return current time in a specific timezone
def get_local_time():
    tz = pytz.timezone('America/Los_Angeles')  
    return datetime.now(tz)


# Recipe model representing submitted recipes
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
    user = db.relationship('User', backref=db.backref('user_recipes', lazy=True), overlaps="author,recipes")
    comments = db.relationship('Comment', backref=db.backref('recipe', lazy=True)) #Relationship to comments (one-to-many)
    tags = db.relationship(
        'Tag',
        secondary=recipe_tags,
        backref=db.backref('recipes', lazy='dynamic'),
        lazy='dynamic'
    )

    # Calculates and returns average rating, or None if no ratings
    @property
    def average_rating(self):
        if not self.rating_count or not self.rating_sum:
            return None
        return round(self.rating_sum / self.rating_count, 1)


#Users have individual display profiles tied to their account (one-to-one relationship), which are optional
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    bio = db.Column(db.Text, nullable=True)
    image_filename = db.Column(db.String(120), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    
#Comment model to create relationship between each recipe and their matching comments
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    commenter = db.Column(db.String(20), nullable=False)
    comment_text = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=get_local_time)
    recipe_id = db.Column(
        db.Integer,
        db.ForeignKey('recipe.id', name='fk_comment_recipe_id'),
        nullable=False
    )

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
