from app import db


# Create association table for many-to-many relationship
memberships = db.Table('memberships',
					   db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
					   db.Column("league_id", db.Integer, db.ForeignKey("league.id")))