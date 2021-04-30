import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import h5py

arquivos=['o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0301_v003-2020m0303t025646.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0302_v003-2020m0304t032738.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0303_v003-2020m0305t141738.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0304_v003-2020m0306t023529.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0305_v003-2020m0307t011802.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0306_v003-2020m0308t032236.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0307_v003-2020m0309t022622.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0308_v003-2020m0310t033323.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0309_v003-2020m0311t042555.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0310_v003-2020m0312t141737.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0311_v003-2020m0313t044332.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0312_v003-2020m0314t032428.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0313_v003-2020m0315t032034.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0314_v003-2020m0316t031816.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0315_v003-2020m0317t032622.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0316_v003-2020m0318t022228.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0317_v003-2020m0319t032417.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0318_v003-2020m0320t120811.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0319_v003-2020m0323t090351.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0320_v003-2020m0323t150524.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0321_v003-2020m0323t150522.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0322_v003-2020m0324t032302.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0323_v003-2020m0325t022014.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0324_v003-2020m0326t141052.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0325_v003-2020m0327t042154.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0326_v003-2020m0330t100825.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0327_v003-2020m0330t100824.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0328_v003-2020m0330t100824.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0329_v003-2020m0331t032001.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0330_v003-2020m0401t031532.he5',
'o3/2020/OMI-Aura_L3-OMDOAO3e_2020m0331_v003-2020m0402t150424.he5']


dados = []
for i in arquivos:
    with h5py.File(i,'r') as f:
        file = f['HDFEOS/GRIDS/ColumnAmountO3/Data Fields/ColumnAmountO3']
        dset = file
        dados.append(file[:])

data=dados[29]
print(data)
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
plt.title('OMI-AURA dia 30/03/2020')
plt.show()