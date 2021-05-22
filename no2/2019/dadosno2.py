import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import h5py

f= h5py.File('no2/2019/OMI-Aura_L2G-OMNO2G_2019m0302_v003-2019m1121t183128.he5', 'r')
dset = f['HDFEOS/GRIDS/ColumnAmountNO2/Data Fields/ColumnAmountNO2']
data = dset[0,:,:]
# Handle fill value.
data[data == dset.fillvalue] = np.nan
data = np.ma.masked_where(np.isnan(data), data)

# Get attributes needed for the plot.
# String attributes actually come in as the bytes type and should
# be decoded to UTF-8 (python3).
title = dset.attrs['Title'].decode()
units = dset.attrs['Units'].decode()

m = Basemap(projection='cyl', resolution='l',  llcrnrlat=-90, urcrnrlat = 90, llcrnrlon=-180, urcrnrlon = 180)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 45.), labels=[0, 0, 0, 1])
 # There is no geolocation data, so construct it ourselves.
longitude = np.arange(0., 1440.0) * 0.25 - 180 + 0.125
latitude = np.arange(0., 720.0) * 0.25 - 90 + 0.125
m.pcolormesh(longitude, latitude, data, latlon=True, cmap='tab20b')
cb = m.colorbar(label='NO2')
plt.title('OMI-AURA dia 02/03/2019')
plt.show()
