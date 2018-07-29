from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)





