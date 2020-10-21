import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#dados do dia 2 de maio de 2014
dados = pd.read_csv(('L_2014_122_1200.dat'),header=None)
#importar cada variavel
u1 = pd.DataFrame(dados,columns=[4])
v1 = pd.DataFrame(dados,columns=[5])
w1 = pd.DataFrame(dados,columns=[6])
ts = pd.DataFrame(dados,columns=[7])
n_bins = 5
#plotar a imagem
plt.hist(u1, bins=n_bins, density=True)

plt.show()