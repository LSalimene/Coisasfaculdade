import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack
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

y=np.fft(u1)
# Number of sample points
s1 = np.multiply(y,y)
s = abs(s1)
N = len(s) #number of elements
n = int(float(N)/2)
pyy= s[0:n]
ny = 20/2
fy1 = np.array(range(0,n))
fy = fy1/n*ny
log = plt.loglog(fy,pyy,'r.')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Densidade Espectral')
plt.title('u1')
plt.show()
