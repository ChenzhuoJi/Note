import matplotlib.pyplot as plt
from numpy import *
x1=arange(-100,-2,0.01)
x2=arange(0.01 ,100,0.01)
y1=(1+1/x1)**x1
y2=(1+1/x2)**x2
plt.figure()
plt.plot(x1,y1,x2,y2)
plt.grid(True)
plt.show()