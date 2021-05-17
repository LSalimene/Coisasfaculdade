import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import h5py

arquivos=['o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0301_v003-2021m0303t012038.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0302_v003-2021m0304t022626.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0303_v003-2021m0305t011801.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0304_v003-2021m0306t014000.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0305_v003-2021m0307t032342.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0306_v003-2021m0308t021842.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0307_v003-2021m0309t032015.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0308_v003-2021m0310t021811.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0309_v003-2021m0311t021713.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0310_v003-2021m0312t011233.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0311_v003-2021m0313t022823.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0312_v003-2021m0314t041926.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0313_v003-2021m0315t032030.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0314_v003-2021m0316t032128.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0315_v003-2021m0317t031751.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0316_v003-2021m0318t031125.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0317_v003-2021m0319t130237.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0318_v003-2021m0320t031909.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0319_v003-2021m0321t021142.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0320_v003-2021m0322t031743.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0321_v003-2021m0323t041824.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0322_v003-2021m0324t031735.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0323_v003-2021m0325t034448.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0324_v003-2021m0326t024554.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0325_v003-2021m0327t031221.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0326_v003-2021m0328t021726.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0327_v003-2021m0329t031140.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0328_v003-2021m0330t042013.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0329_v003-2021m0331t023941.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0330_v003-2021m0401t033209.he5',
'o3/2021/OMI-Aura_L3-OMDOAO3e_2021m0331_v003-2021m0402t033657.he5']


dados = []
for i in arquivos:
    with h5py.File(i,'r') as f:
        file = f['HDFEOS/GRIDS/ColumnAmountO3/Data Fields/ColumnAmountO3']
        dset = file
        dados.append(file[:])

data=dados[30]
# Handle fill value.
data[data == dset.fillvalue] = np.nan
data = np.ma.masked_where(np.isnan(data), data)

m = Basemap(projection='cyl', resolution='l', llcrnrlat=-32.5, urcrnrlat = -30, llcrnrlon=-53, urcrnrlon = -51)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 181., 45.), labels=[0, 0, 0, 1])
 # There is no geolocation data, so construct it ourselves.
longitude = np.arange(0., 1440.0) * 0.25 - 180 + 0.125
latitude = np.arange(0., 720.0) * 0.25 - 90 + 0.125
m.pcolormesh(longitude, latitude, data, latlon=True, cmap='tab20b',shading='auto')
cb = m.colorbar(label='Solução Total de Ozonio')
plt.title('OMI-AURA dia 31/03/2021')
plt.savefig('21dia31.png')
#plt.show()