
# Import necessary form classes and validators from Flask-WTF and WTForms
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField,SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from wtforms.widgets import ListWidget, CheckboxInput

# Import the User model for validation checks
from .models import User

# Custom validator to enforce password complexity rules
def password_requirements(form, field):
    pw = field.data
    if len(pw) < 4 or len(pw) > 32:
        raise ValidationError('Password must be between 4 and 32 characters.')
    if not any(c.isupper() for c in pw):
        raise ValidationError('Password must have at least one uppercase letter.')
    if not any(c.isdigit() for c in pw):
        raise ValidationError('Password must have at least one number.')


class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

# Form for user registration
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=32)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), password_requirements])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # Custom validator to ensure the username is unique
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please choose a different one.')

    # Custom validator to ensure the email is unique
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already registered. Please choose a different one.')

# Form for user login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Form for creating or editing a recipe
class RecipeForm(FlaskForm):
    title = StringField('Recipe Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
    remove_image = BooleanField('Remove current image') 
    submit = SubmitField('Submit Recipe')
    tags = MultiCheckboxField('Tags', coerce=int)


# Form to collect visitor emails before allowing recipe viewing
class VisitorEmailForm(FlaskForm):
    email = StringField('Enter your Email', validators=[DataRequired(), Email()])
    submit = SubmitField('View Recipes')

# Form for users to update their profile information
class ProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=32)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('New Password', validators=[Optional(), password_requirements])
    bio = StringField('User Bio')
    image = FileField('Upload New Profile Image', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
    submit = SubmitField('Update Profile')

# Form for logged in users to add comments to a recipe
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment Text',validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Add Comment')
