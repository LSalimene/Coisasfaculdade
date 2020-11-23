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

y=scipy.fftpack.fft(tv)
# Number of sample points
N = len(y)
pyy1 =abs(y)
pyy = np.multiply(pyy1,pyy1)
ny=20/2
fy1=np.array(range(36000))
fy2 = fy1/(36000)
fy = fy2*ny
plt.plot(pyy,y,'r.')
plt.ylabel('Densidade Espectral')
plt.xlabel('Frequência (Hz)')
plt.title("Densidade Espectral para T")
plt.grid()
plt.show()