import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.style.use('seaborn')

x = [0]
def random_walk(i):
    passox = random.randrange(-1,2,1)
    x.append( x[-1] + passox )
    plt.plot(x, c = 'r')
 
animation = animation.FuncAnimation( fig = plt.figure(), func = random_walk, interval = 2)
plt.show()