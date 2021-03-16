import random  #biblioteca que gera números aleatórios 
import matplotlib.pyplot as plt #biblioteca para conseguir plotar os gráficos 
import matplotlib.animation as animation #biblioteca usada para a animação do randow walk
plt.style.use('seaborn') #estilo do plot
x = [0] #definir posição inicial do x
y = [0] #definir posição inicial do y
def random_walk(i): #criar a função para animar
    passox = random.randrange(-1,2,1) #escolhe um numero aleatório entre -1,0 e 1  para x
    passoy = random.randrange(-1,2,1) #escolhe um numero aleatório entre -1,0 e 1  para y

    x.append( x[-1] + passox) #coloca o passo aleatório, mudando a posição de x
    y.append( y[-1] + passoy) #coloca o passo aleatório, mudando a posição de y
    plt.plot(x,y ,c = 'b') #plota o passo
 
animation = animation.FuncAnimation( fig = plt.figure(), func = random_walk, interval = 1) #cria a animação, mostrando um passo por segundo
plt.show() #mostra o plot