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
#Calular o numero para 20 min

deltat20 = float(mediat22)-float(mediat2)
deltau20 = float(mediau22)-float(mediau2)
deltav20 = float(mediav22)-float(mediav2)


bt = 9.81*deltat20*8
us = deltau20*deltau20
vs = deltav20*deltav20
usvs = us+vs
st = float(mediat2)*float(usvs)

r2= bt/-st

#Calular o numero para 40 min

deltat40 = float(mediat24)-float(mediat4)
deltau40 = float(mediau24)-float(mediau4)
deltav40 = float(mediav24)-float(mediav4)


bt4 = 9.81*deltat40*8
us4 = deltau40*deltau40
vs4 = deltav40*deltav40
usvs4 = us4+vs4
st4 = float(mediat4)*float(usvs4)

r4= bt4/-st4

#Calular o numero para 60 min

deltat60 = float(mediat26)-float(mediat6)
deltau60 = float(mediau26)-float(mediau6)
deltav60 = float(mediav26)-float(mediav6)


bt6 = 9.81*deltat60*8
us6 = deltau60*deltau60
vs6 = deltav60*deltav60
usvs6 = us6+vs6
st6 = float(mediat6)*float(usvs6)

r6= bt6/-st6

#Uestrela
uw20 = float(mediau2)*float(mediaw2)
vw20 = float(mediav2)*float(mediaw2)
uw202 = np.multiply (uw20,uw20)
vw202 = np.multiply (vw20,vw20)
uwvw20 = uw202+vw202
uestrela20=np.sqrt(uwvw20)

uw40 = float(mediau4)*float(mediaw4)
vw40 = float(mediav4)*float(mediaw4)
uw402 = np.multiply (uw40,uw40)
vw402 = np.multiply (vw40,vw40)
uwvw40 = uw402+vw402
uestrela40=np.sqrt(uwvw40)

uw60 = float(mediau6)*float(mediaw6)
vw60 = float(mediav6)*float(mediaw6)
uw602 = np.multiply (uw60,uw60)
vw602 = np.multiply (vw60,vw60)
uwvw60 = uw602+vw602
uestrela60=np.sqrt(uwvw60)


t20=float(mediat2)/1216
t40=float(mediat4)/1216
t60=float(mediat6)/1216


tempo = [20,40,60]
temperatura = [t20,t40,t60]
uestrela=[uestrela20,uestrela40,uestrela60]
plt.plot(tempo,uestrela,'g',label="U*")
plt.hold = True
plt.plot(tempo,temperatura,'r',label='Q')
plt.xlabel('Tempo (min)')
plt.title("U* e Fluxo de calor por Tempo")
plt.grid()
plt.legend()
plt.show()
