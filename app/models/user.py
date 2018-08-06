from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Create association table for many-to-many relationship
# memberships = db.Table('memberships',
# 					   db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
# 					   db.Column("league_id", db.Integer, db.ForeignKey("league.id")))


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

	# Relationships with League
	# Has implicit "leagues" field from many-to-many relationship with League class
	commissioners = db.relationship("League", backref="commissioner", lazy="dynamic")


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


# #####################################################
# #### LEAGUE MODEL ####
# #####################################################

# class League(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	name = db.Column(db.String(128), index=True, unique=True)
# 	size = db.Column(db.Integer, index=True)
#
# 	# Relationships with User
# 	# Has implicit "commissioner" field from one-to-many relationship with User class
# 	members = db.relationship("User", secondary=memberships, backref="leagues", lazy="dynamic")
# 	commissioner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#
# 	def __init__(self, name, size):
# 		self.name = name
# 		self.size = size
#
# 	def __repr__(self):
# 		return "<League: {}>".format(self.name)