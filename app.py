import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Gets the absolute path to the working directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#####################################################
#### ROUTING ####
#####################################################
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/my_team")
def my_team():
    return render_template('my_team.html')


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
#### DATABASES ####
#####################################################
class Players(db.Model):
	# Set table name
	__tablename__ = "players"

	# Create columns of table
	id = db.Column(db.Integer, primary_key=True)


if __name__ == "__main__":
    app.run(debug=True)





