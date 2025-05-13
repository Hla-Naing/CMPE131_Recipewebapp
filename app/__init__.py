
# Import necessary libraries and extensions
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from . import cli

# Initialize Flask extensions 
db = SQLAlchemy()
migrate = Migrate()  
login_manager = LoginManager()
app = None

# Application factory function
def create_app():
    global app

    # Create Flask app instance
    app = Flask(__name__)

    # Configure the secret key for session management and CSRF protection
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Set up the database URI (SQLite) using the current directory
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    cli.register_commands(app)


    # Set the login view for unauthorized users
    login_manager.login_view = 'login'

    # Import and register the route handlers (views)
    from . import routes

    # Create database tables within app context if they don't exist
    with app.app_context():
        db.create_all()

    # Return the fully configured app instance
    return app

