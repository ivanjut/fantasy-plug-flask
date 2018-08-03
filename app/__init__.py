from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


#Instantiate app
app = Flask(__name__)

# Configure secret keys
app.config.from_object(Config)

# Set up database
db = SQLAlchemy(app)
db.create_all()
db.session.commit()
migrate = Migrate(app, db)

# Set up login manager
login_manager = LoginManager(app)
login_manager.login_view = "login"


from app import views
from app.models.user import User