import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import h5py

arquivos=['o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0301_v003-2019m0304t041525.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0302_v003-2019m0304t041532.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0303_v003-2019m0305t010640.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0304_v003-2019m0306t021524.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0305_v003-2019m0307t121159.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0306_v003-2019m0308t075340.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0307_v003-2019m0309t031839.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0308_v003-2019m0310t012029.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0309_v003-2019m0311t033133.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0310_v003-2019m0313t012010.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0311_v003-2019m0313t032121.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0312_v003-2019m0314t140515.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0313_v003-2019m0315t032450.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0314_v003-2019m0316t021914.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0315_v003-2019m0317t032104.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0316_v003-2019m0318t032100.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0317_v003-2019m0319t031030.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0318_v003-2019m0320t031012.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0319_v003-2019m0321t031249.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0320_v003-2019m0322t041011.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0321_v003-2019m0323t150608.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0322_v003-2019m0324t031503.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0323_v003-2019m0325t041422.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0324_v003-2019m0326t031335.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0325_v003-2019m0327t031614.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0326_v003-2019m0328t031403.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0327_v003-2019m0329t140439.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0328_v003-2019m0330t030855.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0329_v003-2019m0331t031039.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0330_v003-2019m0401t021122.he5',
'o3/2019/OMI-Aura_L3-OMDOAO3e_2019m0331_v003-2019m0402t041503.he5',]




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
plt.title('OMI-AURA dia 31/03/2020')
plt.savefig('19dia31.png')
#plt.show()