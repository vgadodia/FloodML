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

def plot_river(ax, lat, lon, river, filename, vmin=None, vmax=None, cbar=True):
    # new_cmap = clr.LinearSegmentedColormap.from_list('blues', arr, N=256)
    plt.pcolormesh(lat, lon, river, vmin=vmin, vmax=vmax, transform=ccrs.PlateCarree())
    if cbar:
        cbar = plt.colorbar(shrink=0.7, orientation="horizontal");
        cbar.set_label('Mean river discharge (m3/s)')
    # plt.show()
    plt.savefig(filename)

def main(lat, lon, river, filename):
    vmin = 0
    vmax = 50

    plt.figure(figsize=(10, 10))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines(resolution='110m')
    ax.stock_img()

    plot_river(ax, lat, lon, river, filename, vmin=vmin, vmax=vmax)


rootgrp = netCDF4.Dataset("./satellite_data/" + "rain" + ".nc4")

# lower_lat, upper_lat = 500, 850
# lower_lon, upper_lon = 2400, 2800

# lat = rootgrp.variables['lat'][lower_lat:upper_lat]
# lon = rootgrp.variables['lon'][lower_lon:upper_lon]
# river = rootgrp.variables["precipitationCal"][0][lower_lat:upper_lat, lower_lon:upper_lon]


lat = rootgrp.variables['lat'][:]
lon = rootgrp.variables['lon'][:]
river = rootgrp.variables["precipitationCal"][0][:]

print(lat.shape, lon.shape, river.shape)

main(lat, lon, river, "file.png")