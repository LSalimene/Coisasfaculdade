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

y=scipy.fftpack.fft(u1)
# Number of sample points

N = tv.shape[0] #number of elements
s = tv 

fft = np.fft.fft(s)
fftfreq = np.fft.fftfreq(len(s))

plt.ylabel("Amplitude")
plt.xlabel("Frequency [Hz]")
plt.plot(fftfreq,fft,'-')
plt.ylim(20.75,22.5)
plt.show()