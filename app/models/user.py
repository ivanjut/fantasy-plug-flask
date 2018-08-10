from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

# #####################################################
# #### USER MODEL ####
# #####################################################

class User(db.Model, UserMixin):
	# Account info
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), index=True, unique=True)
	username = db.Column(db.String(64), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	commissioners = db.relationship("League", backref="commissioner", lazy="dynamic")

	# Implicit "ownerships" field from Ownership association table


	def __init__(self, email, username, password):
		self.email = email
		self.username = username
		self.password_hash = generate_password_hash(password)

	def __repr__(self):
		return '<User: {}>'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def validate_password(self, password):
		return check_password_hash(self.password_hash, password)