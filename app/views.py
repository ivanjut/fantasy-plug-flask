from flask import render_template, redirect, url_for, flash
from app.forms import LoginForm, SignupForm, PlayerForm
from app import app


#####################################################
#### VIEW FUNCTIONS ####
#####################################################
@app.route("/")
def index():
	return render_template("index.html")


@app.route("/my_team", methods=["GET", "POST"])
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
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for("index"))
	return render_template("login.html", form=form)


@app.route("/account_settings")
def account_settings():
	return render_template("account_settings.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		return redirect(url_for("index"))
	return render_template("signup.html", form=form)