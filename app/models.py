from app import db


# #####################################################
# #### DATABASE MODELS ####
# #####################################################
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User: {}>'.format(self.username)


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