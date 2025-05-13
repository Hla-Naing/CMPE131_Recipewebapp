
# Import required modules for routing, forms, database, file handling, etc.
import os
import random
from flask import Flask, render_template, redirect, url_for, flash, session, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from PIL import Image
from sqlalchemy import or_
from . import app, db, login_manager
from .models import User, Recipe, Profile, Comment
from .forms import RegistrationForm, LoginForm, RecipeForm, VisitorEmailForm, ProfileForm, CommentForm

# Helper function to save and resize uploaded images
def save_resized_image(image_file, filename, size=(300, 300)):
    filepath = os.path.join(app.root_path, 'static/uploads', filename)
    img = Image.open(image_file)
    img.thumbnail(size)  
    img.save(filepath)

# Helper function to generate a shuffled list of placeholder colors
def get_placeholder_colors(count):
    colors = [
        "#FF6B6B", "#6BCB77", "#4D96FF", "#FFC75F",
        "#F9F871", "#A393EB", "#FF9671", "#00C9A7",
        "#D65DB1", "#845EC2"
    ]
    random.shuffle(colors)
    return colors[:count]

# Helper function to save and resize profile images
def save_profile_image(image_file):
    filename = secure_filename(image_file.filename)
    filepath = os.path.join(app.root_path, 'static/uploads', filename)

    img = Image.open(image_file)
    img.thumbnail((300, 300))  # Resize
    img.save(filepath)

    return filename

# Callback to load a user by ID (used by Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Injects current_user into all templates
@app.context_processor
def inject_user():
    return dict(current_user=current_user)

# Home page route that displays all recipes (for general viewing)
@app.route('/', methods=['GET','POST'])
def home():
    recipes = Recipe.query.order_by(Recipe.title.asc()).all()
    return render_template('home.html', recipes=recipes)

# Visitor-facing recipe browsing with optional search
@app.route('/visitor_recipes')
def visitor_recipes():
    search_query = request.args.get('q', '')
    if search_query:
        recipes = Recipe.query.filter(
            or_(
                Recipe.title.ilike(f'%{search_query}%'),
                Recipe.ingredients.ilike(f'%{search_query}%')
            )
        ).all()
    else:
        recipes = Recipe.query.all()
    return render_template('visitor_recipes.html', recipes=recipes)

# Login page and logic, checks for existing user info
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('recipes'))
        else:
            flash('Login Unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', form=form)

# Registration page and logic
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Authenticated user's personal recipe dashboard
@app.route('/recipes')
@login_required
def recipes():
    recipes = Recipe.query.filter_by(user_id=current_user.id).all()
    missing_images_count = sum(1 for r in recipes if not r.image_filename)
    placeholder_colors = get_placeholder_colors(missing_images_count)
    return render_template('recipes.html', recipes=recipes, name=current_user.username, placeholder_colors=placeholder_colors)

# Page for creating a new recipe
@app.route('/make_recipe', methods=['GET', 'POST'])
@login_required
def make_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        image_file = form.image.data
        filename = None

        if image_file:
            filename = secure_filename(image_file.filename)
            save_resized_image(image_file, filename, size=(300,300))

        recipe = Recipe(
            title=form.title.data, 
            description=form.description.data,
            ingredients=form.ingredients.data,  
            instructions=form.instructions.data,
            image_filename=filename, 
            user_id=current_user.id
        )
        db.session.add(recipe)
        db.session.commit()
        flash('Recipe created successfully!', 'success')
        return redirect(url_for('recipes'))

    return render_template('new_recipe.html', form=form)

# Display a single recipe's detail page with any additional comments
# @app.route('/recipe/<int:id>', methods=['GET', 'POST'])
# def recipe_details(id):
#     recipe = Recipe.query.get_or_404(id)
#     form = CommentForm()
#     if form.validate_on_submit():
#         new_comment = Comment(
#                 commenter=current_user.username,
#                 comment_text=form.comment.data
#         )
#         db.session.add(new_comment)
#         db.session.commit()
#         flash('Comment posted successfully!', 'success')
#         return redirect('/recipe/<int:id>')
#     return render_template('recipe_details.html', recipe=recipe, form=form)
@app.route('/recipe/<int:id>', methods=['GET', 'POST'])
def recipe_details(id):
    recipe = Recipe.query.get_or_404(id)
    comments = Comment.query.filter_by(recipe_id=recipe.id).order_by(Comment.created.desc()).all()

    form = CommentForm()
    
    if current_user.is_authenticated and form.validate_on_submit():
        new_comment = Comment(
            commenter=current_user.username,
            comment_text=form.comment.data,
            recipe_id=recipe.id  # associate comment with this recipe
        )
        db.session.add(new_comment)
        db.session.commit()
        flash('Comment posted successfully!', 'success')
        return redirect(url_for('recipe_details', id=recipe.id))

    return render_template('recipe_details.html', recipe=recipe, form=form, comments=comments)
# Edit an existing recipe (only allowed by the owner)
@app.route('/edit_recipe/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    
    if recipe.user_id != current_user.id:
        abort(403)

    form = RecipeForm(obj=recipe)
    form.image.label.text = 'Replace Image'

    if form.validate_on_submit():
        recipe.title = form.title.data
        recipe.description = form.description.data
        recipe.ingredients = form.ingredients.data
        recipe.instructions = form.instructions.data
        
        # Handle new image upload
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            save_resized_image(form.image.data, filename, size=(300, 300))
            recipe.image_filename = filename

        # Handle "remove image" checkbox
        elif form.remove_image.data and recipe.image_filename:
            image_path = os.path.join(app.root_path, 'static/uploads', recipe.image_filename)
            if os.path.exists(image_path):
                os.remove(image_path)
            recipe.image_filename = None

        db.session.commit()
        flash('Recipe updated successfully!', 'success')
        return redirect(url_for('recipes'))

    return render_template('edit_recipe.html', form=form, recipe=recipe)

# Delete a recipe (only allowed by the owner)
@app.route('/delete_recipe/<int:id>', methods=['POST'])
@login_required
def delete_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    if recipe.user_id != current_user.id:
        abort(403)
    db.session.delete(recipe)
    db.session.commit()
    flash('Recipe deleted successfully.', 'success')
    return redirect(url_for('recipes'))

# User Profile & Public Routes
@app.route('/profile/<int:user_id>')
def public_profile(user_id):
    user = User.query.get_or_404(user_id)
    profile = Profile.query.filter_by(user_id=user.id).first()
    recipes = Recipe.query.filter_by(user_id=user.id).all()
    return render_template('public_profile.html', user=user, profile=profile, recipes=recipes)

# View another user's public recipes
@app.route('/user/<int:user_id>/recipes')
@login_required
def user_recipes(user_id):
    user = User.query.get_or_404(user_id)
    recipes = Recipe.query.filter_by(user_id=user.id).order_by(Recipe.title.asc()).all()
    return render_template('user_recipes.html', user=user, recipes=recipes)

# View current user's profile
@app.route('/profile')
@login_required
def view_profile():
    profile = Profile.query.filter_by(user_id=current_user.id).first()
    return render_template('profile.html', profile=profile)       

# Edit current user's profile
@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    profile = Profile.query.filter_by(user_id=current_user.id).first()

    # Create profile record if it doesn't exist yet
    if not profile:
        profile = Profile(username=current_user.username, user_id=current_user.id)
        db.session.add(profile)

    form = ProfileForm(obj=profile)

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.password.data:
            current_user.password = form.password.data  
        profile.bio = form.bio.data

        # Handle image upload
        if form.image.data:
            filename = save_profile_image(form.image.data)
            profile.image_filename = filename

        db.session.commit()
        flash("Profile updated successfully.")
        return redirect(url_for('view_profile'))

    return render_template('edit_profile.html', form=form, profile=profile)

# Logout the current user and clear session
@app.route('/logout')
def logout():
    logout_user()
    session.pop('visitor_email', None)
    return redirect(url_for('home'))

# Handle recipe rating submissions
@app.route('/recipe/<int:id>/rate', methods=['POST'])
def rate_recipe(id):
    recipe = Recipe.query.get_or_404(id)

    # Defensive fix for None values
    if recipe.rating_sum is None:
        recipe.rating_sum = 0
    if recipe.rating_count is None:
        recipe.rating_count = 0

    try:
        rating = int(request.form['rating'])
        if rating < 1 or rating > 5:
            flash('Invalid rating. Please select between 1 and 5.', 'danger')
        else:
            recipe.rating_sum += rating
            recipe.rating_count += 1
            db.session.commit()
            flash('Thank you for rating!', 'success')
    except (ValueError, KeyError):
        flash('Invalid rating submission.', 'danger')
    return redirect(url_for('recipe_details', id=recipe.id))

#  About Us route 
@app.route('/about')
def about_us():
    return render_template('about_us.html')
