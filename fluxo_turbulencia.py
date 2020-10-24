import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#dados do dia 2 de maio de 2014
dados = pd.read_csv(('L_2014_122_1200.dat'),header=None)
#importar cada variavel
w1 = pd.DataFrame(dados,columns=[6])
ts = pd.DataFrame(dados,columns=[7])
#plotar a imagem
w1o=np.transpose(ts)

plt.hist(w1o,bins=25,color='r')
plt.xlabel('T (C)')
plt.ylabel('Frequência de Ocorrencia')
plt.show()