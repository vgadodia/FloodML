"""Web app."""
import flask
from flask import Flask, render_template, request, redirect, url_for
from training import prediction
import requests
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
    return render_template('predicts.html')

@app.route('/predicts.html', methods=["GET", "POST"])
def get_predicts():
    cityname = request.form["firstname"]
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    location = cityname
    api_key = 'kDmciXIzDUPncHWYeZtvJ3rdMbLc0w1s8-dxCAhtO2Y' # Acquire from developer.here.com
    PARAMS = {'apikey':api_key,'q':location} 
    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()
    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']
    final = prediction.get_data(latitude, longitude)
    return render_template('predicts.html', message="This will be your desire info about "+str(final))

if __name__ == "__main__":
    app.run(debug=True)