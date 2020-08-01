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

app = flask.Flask(__name__)

data = [{'name':'Delhi', "sel": "selected"}, {'name':'Mumbai', "sel": ""}, {'name':'Kolkata', "sel": ""}, {'name':'Bangalore', "sel": ""}, {'name':'Chennai', "sel": ""}]
# data = [{'name':'India', "sel": ""}]
months = [{"name":"January", "sel": ""}, {"name":"February", "sel": ""}, {"name":"March", "sel": ""}, {"name":"April", "sel": ""}, {"name":"May", "sel": ""}, {"name":"June", "sel": ""}, {"name":"July", "sel": "selected"}]

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
    return render_template('satellite.html', data=data, image="processed_satellite_images/Delhi_July.png", months=months, text="Delhi in January 2020")

@app.route('/satellite.html', methods=['GET', 'POST'])
def satelliteimages():
    place = request.form.get('place')
    date = request.form.get('date')
    data = [{'name':'Delhi', "sel": ""}, {'name':'Mumbai', "sel": ""}, {'name':'Kolkata', "sel": ""}, {'name':'Bangalore', "sel": ""}, {'name':'Chennai', "sel": ""}]
    months = [{"name":"January", "sel": ""}, {"name":"February", "sel": ""}, {"name":"March", "sel": ""}, {"name":"April", "sel": ""}, {"name":"May", "sel": ""}, {"name":"June", "sel": ""}, {"name":"July", "sel": ""}]
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
    print(image)
    return render_template('satellite.html', data=data, image=image, months=months, text=text)

@app.route('/predicts.html')
def predicts():
    return render_template('predicts.html')

@app.route('/predicts.html', methods=["GET", "POST"])
def get_predicts():
    firstname = request.form["firstname"]
    print(firstname) 
    return render_template('predicts.html')

if __name__ == "__main__":
    app.run(debug=True)