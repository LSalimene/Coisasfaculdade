import math
k = 0
c = (0.000000000002426)*(1-math.cos(0.008726646))
x = c + 0.00000000000124

while (x < 0.000000555):
    k = k+1
    x = c+x
    print(x)

print(k)
