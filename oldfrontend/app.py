"""Web app."""
import flask
from flask import Flask, render_template, request, redirect, url_for

app = flask.Flask(__name__)


@app.route("/")
@app.route('/index.html')
def index() -> str:
    """Base page."""
    return flask.render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)