import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

t = np.arange(0,63,3)
u = [3,4,3,6, 6, 2, 5, 3, 7, 8, 5, 4, 3, 5, 2, 2, 4, 5, 3, 6, 5]
u1 = [3,4,3,6, 6, 2, 5, 3, 7, 8, 5, 4, 3, 5, 2, 2, 4, 5, 3, 6, 5]
umean = np.mean(u)
u2 = np.subtract(u,u1)
u3 = u - umean
um = u2 + (umean)
plt.xlim (0,60)
#plt.plot(t,u,label="t vs U")
plt.hold = True
print(umean)
plt.plot(t,um,label=('p vs Ū'))
plt.plot(t,u3,label=("p vs U'")) 
plt.xlabel ('Tempo (s)')
plt.ylabel ('U (m/s)')
plt.legend(loc='best')
plt.grid()
plt.show()
