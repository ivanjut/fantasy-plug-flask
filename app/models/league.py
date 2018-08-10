from app import db
from app.models.ownership import Ownership


# #####################################################
# #### LEAGUE MODEL ####
# #####################################################

class League(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), index=True, unique=True)
	size = db.Column(db.Integer, index=True)
	commissioner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

	# Implicit "ownerships" field from Ownership association table


	def __init__(self, name, size):
		self.name = name
		self.size = size

	def __repr__(self):
		return "<League: {}>".format(self.name)