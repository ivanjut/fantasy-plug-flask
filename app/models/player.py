from app import db


# #####################################################
# #### PLAYER MODEL ####
# #####################################################

class Player(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), index=True)