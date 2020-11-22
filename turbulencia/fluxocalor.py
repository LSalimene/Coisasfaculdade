import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#dados do dia 2 de maio de 2014
dados = pd.read_csv(('/home/lucas/Coisasfaculdade/turbulencia/L_2014_122_1200.dat'),header=None)
#importar cada variavel
ano = pd.DataFrame(dados,columns=[0])
dia = pd.DataFrame(dados,columns=[1])
hhmm = pd.DataFrame(dados,columns=[2])
seg = pd.DataFrame(dados,columns=[3])
u1 = pd.DataFrame(dados,columns=[4])
v1 = pd.DataFrame(dados,columns=[5])
w1 = pd.DataFrame(dados,columns=[6])
tv = pd.DataFrame(dados,columns=[7])
u2 = pd.DataFrame(dados,columns=[14])
v2 = pd.DataFrame(dados,columns=[15])
w2 = pd.DataFrame(dados,columns=[16])
tv2 = pd.DataFrame(dados,columns=[17])
#Fazer as medias para cada 20min
i0=0
#1200=23999, 2400 = 47999, 3600 = 72000
#r = np.where(a == 2400)
r1=11999+1
r2 = 47999+1
r3 = 72000
ts = tv+272.15
ts2 = tv2+272.15


u20 = u1[int(i0):int(r1)]
v20 = v1[int(i0):int(r1)]
w20 = w1[int(i0):int(r1)]
ts20 = ts[int(i0):int(r1)]

u220 = u2[int(i0):int(r1)]
v220 = v2[int(i0):int(r1)]
w220 = w2[int(i0):int(r1)]
ts220 = ts2[int(i0):int(r1)]

u40 = u1[int(r1):int(r2)]
v40 = v1[int(r1):int(r2)]
w40 = w1[int(r1):int(r2)]
ts40 = ts[int(r1):int(r2)]

u240 = u2[int(r1):int(r2)]
v240 = v2[int(r1):int(r2)]
w240 = w2[int(r1):int(r2)]
ts240 = ts2[int(r1):int(r2)]

u260 = u2[int(r2):int(r3)]
v260 = v2[int(r2):int(r3)]
w260 = w2[int(r2):int(r3)]
ts260 = ts2[int(r2):int(r3)]

u60 = u1[int(r2):int(r3)]
v60 = v1[int(r2):int(r3)]
w60 = w1[int(r2):int(r3)]
ts60 = ts[int(r2):int(r3)]

mediau2 = np.mean(u20)
mediav2 = np.mean(v20)
mediaw2 = np.mean(w20)
mediat2 = np.mean(ts20)

mediau22 = np.mean(u220)
mediav22 = np.mean(v20)
mediaw22 = np.mean(w220)
mediat22 = np.mean(ts220)

mediau4 = np.mean(u40)
mediav4 = np.mean(v40)
mediaw4 = np.mean(w40)
mediat4 = np.mean(ts40)

mediau24 = np.mean(u240)
mediav24 = np.mean(v240)
mediaw24 = np.mean(w240)
mediat24 = np.mean(ts240)

mediau6 = np.mean(u60)
mediav6 = np.mean(v60)
mediaw6 = np.mean(w60)
mediat6 = np.mean(ts60)

mediau26 = np.mean(u260)
mediav26 = np.mean(v260)
mediaw26 = np.mean(w260)
mediat26 = np.mean(ts260)