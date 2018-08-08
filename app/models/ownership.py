from app import db


# Association table for users, leagues, and players
# Has three columns: User ID, League ID, Player ID
# Will be a massive data set of all users and which players they own


# EXAMPLE: 2 users, 2 leagues, 3 players
# +---------+-----------+-----------+
# | user_id | league_id | player_id |
# +---------+-----------+-----------+
# +---------+-----------+-----------+
# |       1 |     1     |     1     |
# +---------+-----------+-----------+
# |       2 |     1     |     2     |
# +---------+-----------+-----------+
# |       2 |     2     |     1     |
# +---------+-----------+-----------+
# |       1 |     1     |     3     |
# +---------+-----------+-----------+
# |       1 |     2     |     2     |
# +---------+-----------+-----------+
# |       2 |     2     |     3     |
# +---------+-----------+-----------+


class Ownership(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
	league_id = db.Column(db.Integer, db.ForeignKey("league.id"))
	player_id = db.Column(db.Integer, db.ForeignKey("player.id"))

	db.UniqueConstraint('user_id', 'league_id', 'player_id')
	db.relationship('User', backref='ownerships', lazy='dynamic')
	db.relationship('League', backref='ownerships', lazy='dynamic')
	db.relationship('Player', backref='ownerships', lazy='dynamic')


	def __init__(self, user, league, player):
		self.user_id = user.id
		self.team_id = league.id
		self.role_id = player.id

	def __repr__(self):
		return "<Ownership: User_{0} -- Leauge_{1} -- Player_{2}>".format(self.user_id, self.league_id, self.player_id)


# ownerships = db.Table('memberships',
# 					  db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
# 					  db.Column("league_id", db.Integer, db.ForeignKey("league.id")),
# 					  db.Column("player_id", db.Integer, db.ForeignKey("player.id")))