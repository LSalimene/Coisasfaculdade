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
ts = pd.DataFrame(dados,columns=[7])
p = pd.DataFrame(dados,columns=[11])
#arrumar o tempo dos dados
min = hhmm-1200
mms = min*60
a=np.add(mms,seg)
#densidade
t = 287.058*ts
ptotal=p*1000
rho = np.divide(ptotal,t)
#Tensao de Reynolds
ws=np.mean(w1)
wm=w1-ws

tss=np.mean(ts)
tm=ts-tss

us=np.mean(u1)
um=u1-us

vs=np.mean(v1)
vm=v1-vs

uw=np.multiply(u1,w1)
vw=np.multiply(v1,w1)
uw2=np.multiply(uw,uw)
vw2=np.multiply(vw,vw)
uwmean=np.mean(uw2)
vwmean=np.mean(vw2)

#vwmean2=0.081212*0.081212
#uwmean2=0.189393*0.189393

reynolds2 =  0.182962+0.464828
#U*
tensaoreynolds=np.sqrt(reynolds2)
uestrela=np.divide(tensaoreynolds,rho)
#Fluxo de Calor Turbulento
t1ts=np.multiply(tm,wm)
#fazer o grafico 
plt.xlim (0,1200)
plt.plot(a,t1ts,'r',label="w'Θ' (C m/s)")
plt.hold = True
plt.plot(a,uestrela,'#A0522D',label='U* (m/s)')
plt.grid()
plt.xlabel ('Tempo (s)')
plt.legend(loc='best')
plt.show()