import gmi_daily_v8 as gmi
import matplotlib as mlt
import matplotlib.pyplot as plt
import cartopy 
import cartopy.crs as ccrs
import numpy as np
from netCDF4 import Dataset as nc
import scipy.interpolate as sc

ncdia = nc('oceansat/AQUA_MODIS.20161001.L3m.DAY.NSST.sst.4km.nc','r')
ncnoite = nc('oceansat/AQUA_MODIS.20161001.L3m.DAY.NSST.sst.4km.nc','r')
data = gmi.GMIdaily('oceansat/f35_20161001v8.2.gz')
sstdia = ncdia.variables['sst'][:]
nsst = ncnoite.variables['sst'][:]-1
lon = ncdia.variables['lon'][:]
lat = ncdia.variables['lat'][:]
sstmw = data.variables['sst'][:]
lon1 = data.variables['longitude'][:]
lat1 = data.variables['latitude'][:]
sstmw[sstmw>250] = np.nan
sstmw = np.nanmean(sstmw,2)
sstir = np.concatenate((sstdia,nsst),axis=1)
sstir=np.nanmean(sstir,1)
sstir[sstir>=45]=np.nan
sstir[sstir<=-2]=np.nan
sstiriri = sc.interp2d(lon, lat, sstir); sstiri = sstiriri(lon1, lat1)
ax = plt.axes(projection=cartopy.crs.PlateCarree())
plt.contourf(lon, lat, sstir, cmap='tab20b')
ax.add_feature(cartopy.feature.COASTLINE)
plt.colorbar(label='TSM')
plt.show()