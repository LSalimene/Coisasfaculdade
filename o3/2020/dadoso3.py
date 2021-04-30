import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import h5py

f = h5py.File('o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0301_v003-2020m0303t025646.he5', 'r')
dset = f['HDFEOS/GRIDS/ColumnAmountO3/Data Fields/ColumnAmountO3']
data = dset[:]

# Handle fill value.
data[data == dset.fillvalue] = np.nan
data = np.ma.masked_where(np.isnan(data), data)

# Get attributes needed for the plot.
# String attributes actually come in as the bytes type and should
# be decoded to UTF-8 (python3).
title = dset.attrs['Title'].decode()
units = dset.attrs['Units'].decode()

m = Basemap(projection='cyl', resolution='l', llcrnrlat=-32.5, urcrnrlat = -30, llcrnrlon=-53, urcrnrlon = -51)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 45.), labels=[0, 0, 0, 1])
 # There is no geolocation data, so construct it ourselves.
longitude = np.arange(0., 1440.0) * 0.25 - 180 + 0.125
latitude = np.arange(0., 720.0) * 0.25 - 90 + 0.125
m.pcolormesh(longitude, latitude, data, latlon=True, cmap='tab20b',vmax=450)
cb = m.colorbar(label='Solução Total de Ozonio')
plt.title('OMI-AURA dia 01/03/2020')
plt.show()
