import os
from flask import Flask, render_template, session, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from flask_sqlalchemy import SQLAlchemy

# Gets the absolute path to the working directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Configure secret key
app.config['SECRET_KEY'] = "ilovedro"

# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#####################################################
#### VIEW FUNCTIONS ####
#####################################################
@app.route("/")
def index():
	return render_template('index.html')


@app.route("/my_team", methods=["GET", "POST"])
def my_team():
	form = PlayerForm()
	if form.validate_on_submit():
		return redirect(url_for("my_team"))
	return render_template('my_team.html', form=form)


@app.route("/news")
def news():
	return render_template('news.html')


@app.route("/stats")
def stats():
	return render_template('stats.html')


@app.route("/video")
def video():
	return render_template('video.html')


#####################################################
#### FORM CLASSES ####
#####################################################
class PlayerForm(FlaskForm):
	"""
	Form to add players onto your team
	"""
	player = StringField("Add player")
	submit = SubmitField("Submit")


#####################################################
#### DATABASE MODELS ####
#####################################################
class Players(db.Model):
	# Set table name
	__tablename__ = "players"

	# Create columns of table
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)

	def __init__(self, name):
		"""
		Defines an instance of a Players database table
		"""
		self.name = name

	def __repr__(self):
		"""
		String representation of a single item in the Players database table
		"""
		return self.name


if __name__ == "__main__":
	app.run(debug=True)
