import random
import numpy as np 
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.style.use('seaborn')

x = [0]
y = [0]
z = [0]
def random_walk(i):
    passox = random.randrange(-1,2,1)
    passoy = random.randrange(-1,2,1)
    passoz = random.randrange(-1,2,1)

    x.append( x[-1] + passox )
    y.append( y[-1] + passoy)
    z.append( z[-1] + passoz)
    ax = plt.subplot(1,1,1, projection='3d')
    ax.plot(x,y,z, c = 'b')
 
animation = animation.FuncAnimation( fig = plt.figure(), func = random_walk, interval = 2)
plt.show()