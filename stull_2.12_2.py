import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Dados do exercicio
w=[0.5,-0.5,1,0.8,0.9,-0.2,-0.5,0,-0.9,-0.1]
t=[295,293,295,298,292,294,292,289,293,299]
ws=np.mean(w)
wm=w-ws
ts=np.mean(t)
tm=t-ts
w2=np.multiply(wm,wm)
t2=np.multiply(tm,tm)
print(w,t,ws,ts,w2,t2,wm,tm)