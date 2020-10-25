import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#dados do dia 2 de maio de 2014
dados = pd.read_csv(('L_2014_122_1200.dat'),header=None)
#importar cada variavel
w1 = pd.DataFrame(dados,columns=[6])
ts = pd.DataFrame(dados,columns=[7])
#arrumar os dados
w1s=np.transpose(w1)
w1m=np.mean(w1)
w1d=w1s+int(w1m)
tss=np.transpose(ts)
tsm=np.mean(ts)
tsd=tss-int(tsm)
t1ts=np.multiply(tsd,w1d)
#plotar a imagem
plt.hist(t1ts,bins=35,color='g')

plt.xlabel("w'Θ' (K m/s)")
plt.ylabel('Frequência de Ocorrencia')
plt.show()