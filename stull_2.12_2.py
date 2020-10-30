import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Dados do exercicio
w=[0.5,-0.5,1,0.8,0.9,-0.2,-0.5,0,-0.9,-0.1]
t=[295,293,295,298,292,294,292,289,293,299]
#Contas pedidas no exercico
ws=np.mean(w)
wm=w-ws
ts=np.mean(t)
tm=t-ts
w2=np.multiply(wm,wm)
t2=np.multiply(tm,tm)
wt=np.multiply(w,t)
wtd=np.multiply(wm,tm)
wt_total=wt+wtd
ubd=np.std(t) #unbiased standard deviation
r2=np.corrcoef(t,w)
print(np.mean(wtd))