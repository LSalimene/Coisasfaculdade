## P. R. del Santoro para  Fis. Comp. IMEF/FURG 02/20
import random as rd                 # Importa biblioteca random
import matplotlib.pyplot as plt     # Importa biblioteca matplotlib.pyplot

N=1000     #  Numero de Passos

dist=[]   # Cria uma "lista vazia"

d=0.0     # Posicao Inicial

for n in range(N): 
   print (N)  
   x=rd.random() # Sorteia numero entre 0.0 e 1.0
   if x > 0.5:   # Verifica se x maior ou menor que 0.5
      passo =1.0 # Se x > 0.5 o passo  a direita
   else :
      passo =-1.0 # Se x < 0.5 o passo a esquerda
   d=d+passo  # distancia no "'n-esimo " passo
   print (N) 
   print (x,passo, d)
   dist.append(d) # adiciona d a lista

plt.plot(dist) # desennha lista posicao na vertical mumero do passoa na horizontal
plt.show()

