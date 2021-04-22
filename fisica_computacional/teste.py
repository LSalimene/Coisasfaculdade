import numpy as np #importar o pacote numpy
from matplotlib import pyplot as plt #importar a função pyplot do pacote matplotlib

#condições iniciais para o metodo de Euler
x0 = 0 #criar um intervalo entre 0 e 10 para a constante de decaimento
n0 = 1 #valor inicial de atomos no instante t
xf = 10 #criar um intervalo entre 0 e 10 para a constante de decaimento
p = 1000 #numero de pontos
deltax = (xf-x0)/(p-1)

x = np.linspace (x0,xf,p) #criar o vetor x para depois gerar os valores de y

n = np.zeros ([p]) #armazenar os valores de n
n[0] = n0

#loop para a solução pelo metodo de Euler
for i in range (1,p):
   n[i] = deltax*(-n[i-1] *x[i-1]) + n[i-1]

for i in range (p):
   print(x[i],n[i])

plt.plot(x,n,'g.')
plt.xlabel('Valor de beta')
plt.ylabel('Numero de atomos no tempo t')
plt.title ( ' Solução aproximada pela metodo de Euler ' )
plt.show()