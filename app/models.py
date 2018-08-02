from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

# #####################################################
# #### DATABASE MODELS ####
# #####################################################
class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), index=True, unique=True)
	username = db.Column(db.String(64), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __init__(self, email, username, password):
		self.email = email
		self.username = username
		self.password_hash = generate_password_hash(password)

	def __repr__(self):
		return '<User: {}>'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

# class Players(db.Model):
# 	# Set table name
# 	__tablename__ = "players"
#
# 	# Create columns of table
# 	id = db.Column(db.Integer, primary_key=True)
# 	name = db.Column(db.Text)
#
# 	def __init__(self, name):
# 		"""
# 		Defines an instance of a Players database table
# 		"""
# 		self.name = name
#
# 	def __repr__(self):
# 		"""
# 		String representation of a single item in the Players database table
# 		"""
# 		return self.name