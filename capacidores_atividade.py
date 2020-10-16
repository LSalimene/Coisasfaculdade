#Importar os pacotes que iremos utilizar
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

k=[2.3, 3.449, 4.6, 5.75, 6.899, 8.049, 9.2, 10.35, 11.5]
c0=[2.3,3.44,4.59,5.74,6.89,8.03,9.18,10.33,11.48]
data=[[1,1.5,2,2.5,3,3.5,4,4.5,5],
[2.3, 3.449, 4.6, 5.75, 6.899, 8.049, 9.2, 10.35, 11.5]]
#escolher o estilo que iremos usar
plt.style.use('ggplot')
#plotar o grafico e escolher a cor e o estilo de plot
ax=plt.subplot(2, 1, 1)

plt.plot(c0,k,c0,k,'bo')
r=r2_score(c0,k)
#nomear os eixos e dar o titulo
plt.xlabel('Capacitancia')
plt.ylabel('Constante Dielétrica')
plt.title('Capacitancia por k')
plt.text(2,5,'r²=0.99')
ax=plt.subplot(2, 1, 2)
# hide axes
ax.axis('off')
ax.axis('tight')
plt.table(data,rowLabels=('k','C0'),loc='center')
#mostrar o grafico
k=[1*2.3,1.5*2.3,2*2.3,2.5*2.3,3*2.3,3.5*2.3,4*2.3,4.5*2.3,5*2.3]
print(k)

plt.show()