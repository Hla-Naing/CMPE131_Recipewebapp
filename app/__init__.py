
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
app = None

def create_app():
    global app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')

    db.init_app(app)
    login_manager.init_app(app)

    from . import routes

    with app.app_context():
        db.create_all()

    return app

