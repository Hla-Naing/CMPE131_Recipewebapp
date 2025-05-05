
from flask import Flask, Blueprint,render_template, redirect, url_for, flash, session, request
from app.forms import RegistrationForm, LoginForm, RecipeForm, VisitorEmailForm, ProfileForm
from app.models import db, User, Recipe, Profile
from flask_login import login_user, logout_user, login_required, current_user
import os

app = Flask(__name__)
app.secret_key = 'your_super_secret_key_here'

bp = Blueprint('main', __name__)

@bp.context_processor
def inject_user():
    return dict(current_user=current_user)

@bp.route('/', methods=['GET','POST'])
def home():
    recipes = Recipe.query.order_by(Recipe.created.desc()).all()
    return render_template('home.html', recipes=recipes)

@bp.route('/visitor_recipes')
def visitor_recipes():
    if 'visitor_email' not in session:
        return redirect(url_for('home'))
    search_query = request.args.get('q', '')  
    if search_query:
        recipes = Recipe.query.filter(Recipe.title.ilike(f'%{search_query}%')).all()
    else:
        recipes = Recipe.query.all()
    return render_template('visitor_recipes.html', recipes=recipes)

@bp.route('/login', methods=['GET','POST'])
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

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/recipes')
@login_required
def recipes():
    recipes = Recipe.query.filter_by(user_id=current_user.id).all()
    return render_template('recipes.html', recipes=recipes, name=current_user.username)

@bp.route('/make_recipe', methods=['GET', 'POST'])
@login_required
def make_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(
            title=form.title.data, 
            description=form.description.data,
            ingredients=form.ingredients.data,  
            instructions=form.instructions.data, 
            user_id=current_user.id
        )
        db.session.add(recipe)
        db.session.commit()
        flash('Recipe created successfully!', 'success')
        return redirect(url_for('recipes'))
    return render_template('new_recipe.html', form=form)

@app.route('/recipe/<int:id>')
def recipe_details(id):
    recipe = Recipe.query.get_or_404(id)
    return render_template('recipe_details.html', recipe=recipe)

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

@app.route('/user/<int:user_id>/recipes')
@login_required
def user_recipes(user_id):
    user = User.query.get_or_404(user_id)
    recipes = Recipe.query.filter_by(user_id=user.id).order_by(Recipe.title.asc()).all()
    return render_template('user_recipes.html', user=user, recipes=recipes)

@bp.route('/profile', methods=['POST'])
@login_required
def view_profile():
    profile = Profile.query.filter_by(user_id=current_user.id).all()
    recipes = Recipe.query.filter_by(user_id=current_user.id).all()
    return render_template('profile.html',profile=profile,recipes=recipes)

@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    #update database for display info on profile
    form = ProfileForm()
    if form.validate_on_submit():
        profile = Profile(id=form.id.data, username=form.username.data, bio=form.bio.data, user_id=current_user.id)
        profile.bio = form.bio.data
        db.session.commit()
        flash("Profile updated.")
    return render_template('edit_profile.html',form=form)
    
@bp.route('/logout')
def logout():
    logout_user()
    session.pop('visitor_email', None)
    return redirect(url_for('home'))



# if __name__ == '__main__':
#     app.run(debug=True)