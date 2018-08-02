from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Instantiate app
app = Flask(__name__)

# Configure secret keys
app.config.from_object(Config)

# Set up database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models