"""Web app."""
import flask
from flask import Flask, render_template, request, redirect, url_for

app = flask.Flask(__name__)


@app.route("/")
@app.route('/index.html')
def index() -> str:
    """Base page."""
    return flask.render_template("index.html")

@app.route('/plots.html')
def plots():
    return render_template('plots.html')

@app.route('/binary.html')
def binary():
    return render_template('binary.html')

@app.route('/heatmaps.html')
def heatmaps():
    return render_template('heatmaps.html')

@app.route('/predicts.html')
def predicts():
    return render_template('predicts.html', message="This will be your desire info about")

@app.route('/predicts.html', methods=["GET", "POST"])
def get_predicts():
    firstname = request.form["firstname"]
    print(firstname) 
    return render_template('predicts.html')

if __name__ == "__main__":
    app.run(debug=True)