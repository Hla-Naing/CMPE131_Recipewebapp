from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
#Needed to run program, including databases and forms


myapp_obj=Flask(__name__)
from app import routes, models

#Add secret key if necessary later on
