import matplotlib as mlt
import matplotlib.pyplot as plt
import cartopy 
import cartopy.crs as ccrs
import numpy as np
from netCDF4 import Dataset as nc
import scipy.interpolate as sc

data = nc('oceansat/dataset-duacs-nrt-global-merged-allsat-phy-l4_1621348767065.nc','r')
sla = data.variables['sla'][0,:,:]
err = data.variables['err'][0,:,:]
lon = data.variables['longitude'][:]
lat = data.variables['latitude'][:]
ax = plt.axes(projection=cartopy.crs.PlateCarree())
plt.pcolormesh(lon, lat, err, cmap='plasma')
ax.add_feature(cartopy.feature.COASTLINE)
plt.colorbar(label='m')
plt.title ('Anomalia de altura do mar')
plt.show()