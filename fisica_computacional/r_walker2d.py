import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
x = [0]
y = [0]
def random_walk(i):
    passox = random.randrange(-1,2,1)
    passoy = random.randrange(-1,2,1)
    passoz = random.randrange(-1,2,1)

    x.append( x[-1] + passox )
    y.append( y[-1] + passoy)
    plt.plot(x,y ,c = 'b')
 
animation = animation.FuncAnimation( fig = plt.figure(), func = random_walk, interval = 2)
plt.show()