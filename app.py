"""Web app."""
import flask
from flask import Flask, render_template, request, redirect, url_for
import netCDF4
import base64

import matplotlib as mpl
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import netCDF4
from matplotlib.axes import Axes
from cartopy.mpl.geoaxes import GeoAxes
GeoAxes._pcolormesh_patched = Axes.pcolormesh
import numpy as np
import matplotlib.path as mpath
import cartopy.feature
import matplotlib.colors as clr

from training import prediction
import requests
app = flask.Flask(__name__)

data = [{'name':'Delhi', "sel": "selected"}, {'name':'Mumbai', "sel": ""}, {'name':'Kolkata', "sel": ""}, {'name':'Bangalore', "sel": ""}, {'name':'Chennai', "sel": ""}]
# data = [{'name':'India', "sel": ""}]
months = [{"name":"May", "sel": ""}, {"name":"June", "sel": ""}, {"name":"July", "sel": "selected"}]
cities = [{'name':'Delhi', "sel": "selected"}, {'name':'Mumbai', "sel": ""}, {'name':'Kolkata', "sel": ""}, {'name':'Bangalore', "sel": ""}, {'name':'Chennai', "sel": ""}]

@app.route("/")
@app.route('/index.html')
def index() -> str:
    """Base page."""
    return flask.render_template("index.html")

@app.route('/plots.html')
def plots():
    return render_template('plots.html')

@app.route('/heatmaps.html')
def heatmaps():
    return render_template('heatmaps.html')

@app.route('/satellite.html')
def satellite():
    direc = "processed_satellite_images/Delhi_July.png"
    with open(direc, "rb") as image_file:
        image = base64.b64encode(image_file.read())
    image = image.decode('utf-8')
    return render_template('satellite.html', data=data, image_file=image, months=months, text="Delhi in January 2020")

@app.route('/satellite.html', methods=['GET', 'POST'])
def satelliteimages():
    place = request.form.get('place')
    date = request.form.get('date')
    data = [{'name':'Delhi', "sel": ""}, {'name':'Mumbai', "sel": ""}, {'name':'Kolkata', "sel": ""}, {'name':'Bangalore', "sel": ""}, {'name':'Chennai', "sel": ""}]
    months = [{"name":"May", "sel": ""}, {"name":"June", "sel": ""}, {"name":"July", "sel": ""}]
    for item in data:
        if item["name"] == place:
            item["sel"] = "selected"
    
    for item in months:
        if item["name"] == date:
            item["sel"] = "selected"

    text = place + " in " + date + " 2020"

    direc = "processed_satellite_images/{}_{}.png".format(place, date)
    with open(direc, "rb") as image_file:
        image = base64.b64encode(image_file.read())
    image = image.decode('utf-8')
    return render_template('satellite.html', data=data, image_file=image, months=months, text=text)

@app.route('/predicts.html')
def predicts():
    return render_template('predicts.html', cities=cities)

@app.route('/predicts.html', methods=["GET", "POST"])
def get_predicts():
    cityname = request.form.get('place')
    cities = cities = [{'name':'Delhi', "sel": ""}, {'name':'Mumbai', "sel": ""}, {'name':'Kolkata', "sel": ""}, {'name':'Bangalore', "sel": ""}, {'name':'Chennai', "sel": ""}]
    for item in cities:
        if item['name'] == cityname:
            item['sel'] = 'selected'
    print(cityname)
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    location = cityname
    api_key = 'Bwv2FJJQHT4FTQBWFC7IEKRE49lNYtrAti6NK7uJVCY' # Acquire from developer.here.com
    PARAMS = {'apikey':api_key,'q':location} 
    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()
    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']
    final = prediction.get_data(latitude, longitude)
    return render_template('predicts.html', cities=cities, temp=str(final[0]), maxt=str(final[1]), wspd=str(final[2]), cloudcover=str(final[3]), percip=str(final[4]), humidity=str(final[5]))

if __name__ == "__main__":
    app.run(debug=True)