from app import db
# from app.models.ownership import Ownership


# #####################################################
# #### LEAGUE MODEL ####
# #####################################################

class League(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), index=True, unique=True)
	size = db.Column(db.Integer, index=True)

	# Relationships with User
	# Has implicit "commissioner" field from one-to-many relationship with User class
	# members = db.relationship("User", secondary=ownerships, backref="leagues", lazy="dynamic")
	commissioner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

	# Relationships with Player
	# players = db.relationship("Player", secondary=ownerships, backref="leagues", lazy="dynamic")


	def __init__(self, name, size):
		self.name = name
		self.size = size

	def __repr__(self):
		return "<League: {}>".format(self.name)