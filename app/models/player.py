from app import db


# #####################################################
# #### PLAYER MODEL ####
# #####################################################

class Player(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), index=True)

	# Implicit "ownerships" field from Ownership association table


	def __init__(self):
		pass

	def __repr__(self):
		return "<Player: {}>".format(self.name)