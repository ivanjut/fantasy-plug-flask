from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

#Instantiate app
app = Flask(__name__)

# Configure secret keys
app.config.from_object(Config)

# Set up database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# # Set up login manager
# login = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view("login")

from app import views, models