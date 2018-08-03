from app import app, db
from flask import render_template, redirect, url_for, flash, request
from app.forms import LoginForm, SignupForm, PlayerForm
from flask_login import current_user, login_user, logout_user, login_required

from app.models.user import User


#####################################################
#### VIEW FUNCTIONS ####
#####################################################
@app.route("/")
def index():
	return render_template("index.html")


@app.route("/my_team", methods=["GET", "POST"])
@login_required
def my_team():
	form = PlayerForm()
	if form.validate_on_submit():
		return redirect(url_for("my_team"))
	return render_template("my_team.html", form=form)


@app.route("/news")
def news():
	return render_template("news.html")


@app.route("/stats")
def stats():
	return render_template("stats.html")


@app.route("/video")
def video():
	return render_template("video.html")


@app.route("/login", methods=["GET", "POST"])
def login():
	# Check to see if user already logged in
	if current_user.is_authenticated:
		flash("Already logged in.")
		return redirect(url_for("index"))

	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is not None and user.validate_password(form.password.data):
			login_user(user, remember=form.remember_me.data)
			flash("Logged in successfully.")

			# Redirect user to page they were trying to access
			next = request.args.get("next")
			if next is None or next[0] != "/":
				next = url_for("index")
			return redirect(next)

		else:
			flash("Invalid username or password.")
			return redirect(url_for("login"))

	return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
	logout_user()
	flash("Logged out.")
	return redirect(url_for("index"))


@app.route("/account_settings")
@login_required
def account_settings():
	return render_template("account_settings.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
					username=form.username.data,
					password=form.password.data)

		# Add user to database
		db.session.add(user)
		db.session.commit()

		flash("Thanks for signing up!")
		return redirect(url_for("login"))
	return render_template("signup.html", form=form)