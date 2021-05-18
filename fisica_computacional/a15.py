# P. R. del Santoro para  Fis. Comp. IMEF/FURG 02/20

import numpy as np                 # Importa biblioteca  nunpy 
import matplotlib.pyplot as plt    # Importa biblioteca matplotlib.pyplot
import random as rd


def IteraV2(Y0,lamb,Nit):
    for n in range(Nit):
      Y1= lamb*Y0*(1.0-Y0)
      Y0=Y1
    return Y1


Nl=300
Npy=300
Nit=1000

lbmin=3.8
lbmax=3.9


LB=np.linspace(lbmin,lbmax,Nl)
for l in LB:
    Y=np.random.rand(Npy)
    Y=IteraV2(Y,l,Nit)
    L=l*np.ones(len(Y)) 
    plt.scatter(L,Y,s=0.1,c='r')       

tx=' Nl='+str(Nl)+'  '+' Ny='+str(Npy)+'  '+'Nit='+str(Nit)
plt.title(tx)
plt.xlim(lbmin,lbmax)
plt.ylim(0.0,1.0)
plt.xlabel('Lambda')    
plt.ylabel('Atractor')  
#
plt.show()

