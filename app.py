from flask import Flask, render_template


app = Flask(__name__)




@app.route('/')
def index():
    return render_template("index.html")


@app.route("/memes")
def memes():
    return render_template('memes.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/HistoryMemes")
def HistoryMemes():
    return render_template('HistoryMemes.html')

@app.route("/WorldWar")
def WorldWar():
    return render_template('WorldWar.html')

@app.route("/Communist")
def Communist():
    return render_template('Communist.html')


@app.errorhandler(404)
def handler404(_):
    return render_template('404.html')


if __name__ == "__main__":
    app.run()