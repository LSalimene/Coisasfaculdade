import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#dados do dia 2 de maio de 2014
dados = pd.read_csv(('L_2014_122_1200.dat'),header=None)
#importar cada variavel
ano = pd.DataFrame(dados,columns=[0])
dia = pd.DataFrame(dados,columns=[1])
hhmm = pd.DataFrame(dados,columns=[2])
seg = pd.DataFrame(dados,columns=[3])
u1 = pd.DataFrame(dados,columns=[4])
v1 = pd.DataFrame(dados,columns=[5])
w1 = pd.DataFrame(dados,columns=[6])
ts = pd.DataFrame(dados,columns=[7])
co2 = pd.DataFrame(dados,columns=[8])
h2o = pd.DataFrame(dados,columns=[9])
p = pd.DataFrame(dados,columns=[11])
#arrumar o tempo dos dados
min = hhmm-1200
mms = min*60
a=np.add(mms,seg)
i0=0
#600=11999, 1200=23999, 1750=34999
r=11999+1
r2=23999+1
r3=23999+1
u10 = u1[int(i0):int(r)]
u20 = u1[int(i0):int(r2)]
u30 = u1[int(i0):int(r3)]

v10 = v1[int(i0):int(r)]
v20 = v1[int(i0):int(r2)]
v30 = v1[int(i0):int(r3)]

w10 = w1[int(i0):int(r)]
w20 = w1[int(i0):int(r2)]
w30 = w1[int(i0):int(r3)]

t10 = a [int(i0):int(r)]
mediau10 = np.mean(u10)
mediau20 = np.mean(u20)
mediau30 = np.mean(u30)
mediau = np.mean(u1)

mediav10 = np.mean(v10)
mediav20 = np.mean(v20)
mediav30 = np.mean(v30)
mediav = np.mean(v1)

mediaw10 = np.mean(w10)
mediaw20 = np.mean(w20)
mediaw30 = np.mean(w30)
mediaw = np.mean(w1)


data = [[ float(mediau10), float(mediau20),  float(mediau30), float(mediau)],
        [ float(mediav10), float(mediav20),  float(mediav30), float(mediav)],
        [ float(mediaw10), float(mediaw20),  float(mediaw30), float(mediaw)]]

rows = [(600, 1200, 1750,3600)]
columns = ('U1', 'V1', 'W1')
fig, ax = plt.subplots()
# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

plt.table(data,loc='center',colLabels=('10 Min', '20 Min', '30 Min','60 Min'),rowLabels=('U1','V1','W1'),rowColours=('r','b','g'))

plt.show()
