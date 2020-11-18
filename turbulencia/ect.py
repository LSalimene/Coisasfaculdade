import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
#arrumar o tempo dos dados
min = hhmm-1200
mms = min*60
a=np.add(mms,seg)
#Fazer as medias para cada 20min
i0=0
#1200=23999, 2400 = 47999, 3600 = 72000
#r = np.where(a == 2400)
r1=11999+1
r2 = 47999+1
r3 = 72000


u20 = u1[int(i0):int(r1)]
v20 = v1[int(i0):int(r1)]
w20 = w1[int(i0):int(r1)]

u40 = u1[int(r1):int(r2)]
v40 = v1[int(r1):int(r2)]
w40 = w1[int(r1):int(r2)]

u60 = u1[int(r2):int(r3)]
v60 = v1[int(r2):int(r3)]
w60 = w1[int(r2):int(r3)]

mediau2 = np.mean(u20)
mediav2 = np.mean(v20)
mediaw2 = np.mean(w20)

mediau4 = np.mean(u40)
mediav4 = np.mean(v40)
mediaw4 = np.mean(w40)

mediau6 = np.mean(u60)
mediav6 = np.mean(v60)
mediaw6 = np.mean(w60)
#Calcular a energia para 20 min
media20v2= mediav2*mediav2
media20u2= mediau2*mediau2
media20w2= mediaw2*mediaw2
media20uv = sum(media20u2,media20v2)
ect201 = sum(media20uv,media20w2)

#Calcular a energia para 40 min
media40v2= mediav4*mediav4
media40u2= mediau4*mediau4
media40w2= mediaw4*mediaw4
media40uv = sum(media40u2,media40v2)
ect401 = sum(media40uv,media40w2)

#Calcular a energia para 20 min
media60v2= mediav6*mediav6
media60u2= mediau6*mediau6
media60w2= mediaw6*mediaw6
media60uv = sum(media60u2,media60v2)
ect601 = sum(media60uv,media60w2)


ect20=(ect201*0.5)
ect40=(ect401*0.5)
ect60=(ect601*0.5)


