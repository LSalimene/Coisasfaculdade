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

mediau20 = -np.mean(u20)+u20
mediav20 = -np.mean(v20)+v20
mediaw20 = -np.mean(w20)+w20

mediau40 = -np.mean(u40)+u40
mediav40 = -np.mean(v40)+v40
mediaw40 = -np.mean(w40)+w40

mediau60 = -np.mean(u60)+u60
mediav60 = -np.mean(v60)+v60
mediaw60 = -np.mean(w60)+w40

#Calcular a energia para 20 min
media20u2 = np.multiply(mediau20,mediau20)
media20v2 = np.multiply(mediav20,mediav20)
media20w2 = np.multiply(mediaw20,mediaw20)
media20uv = sum(media20u2,media20v2)
ect201 = sum(media20uv,media20w2)

#Calcular a energia para 40 min
media40u2= np.multiply(mediau40,mediau40)
media40v2= np.multiply(mediav40,mediav40)
media40w2= np.multiply(mediaw40,mediaw40)
media40uv = sum(media40u2,media40v2)
ect401 = sum(media40uv,media40w2)

#Calcular a energia para 20 min
media60u2= np.multiply(mediau60,mediau60)
media60v2= np.multiply(mediav60,mediav60)
media60w2= np.multiply(mediaw60,mediaw60)
media60uv = sum(media60u2,media60v2)
ect601 = sum(media60uv,media60w2)

#Calcular o numero 
richard = np.mean(ect201)
richardd = np.mean(ect401)
richarddd = np.mean(ect601)

ect20=(richard*0.5)
ect40=(richardd*0.5)
ect60=(richarddd*0.5)

print(ect20,ect40,ect60)

ect = [2.596443,2.590203,2.599637]
tempo = [20,40,60]
plt.plot(tempo,ect)
plt.show()