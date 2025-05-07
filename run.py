from app.forms import RecipeForm, LoginForm, RegistrationForm
from app.models import db, User, Recipe
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

