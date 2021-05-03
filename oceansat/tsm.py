import gmi_daily_v8 as gmi
import matplotlib as mlt
import matplotlib.pyplot as plt
import cartopy 
import cartopy.crs as ccrs
import numpy as np
from netCDF4 import Dataset as nc

ncdia = nc('oceansat/AQUA_MODIS.20161001.L3m.DAY.NSST.sst.4km.nc','r')
ncnoite = nc('oceansat/AQUA_MODIS.20161001.L3m.DAY.NSST.sst.4km.nc','r')
data = gmi.GMIdaily('oceansat/f35_20161001v8.2')
sstdia = ncdia.variables['sst'][:]
nsst = ncnoite.variables['sst'][:]
lon = ncdia.variables['lon'][:]
lat = ncdia.variables['lat'][:]

sstir = np.concatenate((sstdia,nsst),axis=1)
sstir=np.nanmean(sstir,1)
sstir[sstir>=45]=np.nan
sstir[sstir<=-2]=np.nan
sstir = np.flipud(sstir)
ax = plt.axes(projection=cartopy.crs.PlateCarree())
plt.contourf(lon, lat, sstdia, cmap='tab20b',shading='auto')
ax.add_feature(cartopy.feature.COASTLINE)
plt.colorbar(label='TSM')

plt.show()