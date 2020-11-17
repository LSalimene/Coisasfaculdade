import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#dados do dia 2 de maio de 2014
dados = pd.read_csv(('L_2014_122_1200.dat'),header=None)
#importar cada variavel
w1 = pd.DataFrame(dados,columns=[6])
ts = pd.DataFrame(dados,columns=[7])
#arrumar os dados
tss=np.transpose(ts)
#calcular a media
tsm=np.mean(ts)
tsd=tss-int(tsm)
#plotar a imagem
plt.hist(tsd,bins=35,color='r')
plt.grid()
plt.xlabel("Θ' (C)") 
plt.ylabel('Frequência de Ocorrencia')
plt.show()