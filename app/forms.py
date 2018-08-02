from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


#####################################################
#### FORM CLASSES ####
#####################################################
class LoginForm(FlaskForm):
	"""
	For for a user to login
	"""
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')


class SignupForm(FlaskForm):
	"""
	Form for a user to sign up
	"""
	email = StringField("Email")
	username = StringField("Username")
	password = StringField("Password")
	submit = SubmitField("Create Account")


class PlayerForm(FlaskForm):
	"""
	Form to add players onto your team
	"""
	player = StringField("Add player")
	submit = SubmitField("Submit")