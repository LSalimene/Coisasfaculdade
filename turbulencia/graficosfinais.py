import matplotlib.pyplot as plt


ue	= (0.2,0.3,0.4)
U2	= (0.04, 0.09, 0.16)
ECT	 = (2.6, 2.5 , 2.6)
Ri	= (-0.5 , -0.4 , -0.5)
t = (10,30,50)

plt.style.use('ggplot')
plt.subplot(4,2,1)
plt.plot(t,ue,'r',t,ue,'k.')
plt.xlabel('Tempo')
plt.ylabel('U*')
plt.title("U* por tempo")
plt.hold = True
plt.subplot(4,2,2)
plt.plot(t,U2,'r',t,U2,'k.')
plt.xlabel('Tempo')
plt.ylabel('U*^2')
plt.title("U*^2 por tempo")

plt.subplot(2,2,3)
plt.plot(t,ECT,'r',t,ECT,'k.')
plt.xlabel('Tempo')
plt.ylabel('ECT')
plt.title("ECT por tempo")

plt.subplot(2,2,4)
plt.plot(t,Ri,'r',t,Ri,'k.')
plt.xlabel('Tempo')
plt.ylabel('Ri')
plt.title("Numero de Richardson por tempo")
plt.show()
