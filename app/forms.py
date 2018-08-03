from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from app.models.user import User


#####################################################
#### FORM CLASSES ####
#####################################################
class LoginForm(FlaskForm):
	"""
	Form for a user to login
	"""
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Log In')


class SignupForm(FlaskForm):
	"""
	Form for a user to sign up
	"""
	email = StringField("Email", validators=[DataRequired(), Email()])
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired(), EqualTo("password_confirm", message="Passwords must match.")])
	password_confirm = PasswordField("Confirm Password", validators=[DataRequired()])
	submit = SubmitField("Create Account")

	def check_email(self, field):
		"""
		Checks if email already exists in the database
		"""
		if User.query.filter_by(email=field.data).first():
			raise ValidationError("Account with that email already exists.")

	def check_username(self, field):
		"""
		Checks if username already exists in the database
		"""
		if User.query.filter_by(username=field.data).first():
			raise ValidationError("Username is taken.")


class PlayerForm(FlaskForm):
	"""
	Form to add players onto your team
	"""
	player = StringField("Add player")
	submit = SubmitField("Submit")