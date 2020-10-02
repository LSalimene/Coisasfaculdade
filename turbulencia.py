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
#plotar a imagem
plt.style.use('bmh')
plt.plot(a,ts,'#A0522D')
plt.hold = True
plt.xlabel('Segundos')
plt.ylabel('Temperatura')
plt.title('temperatura por tempo')
#desconsiderar tempos maiores que uma hora para o grafico ficar mais bonito
plt.xlim (0,3600)
plt.show()
