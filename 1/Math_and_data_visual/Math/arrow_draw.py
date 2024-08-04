from matplotlib import pyplot as plt
from math import *
import numpy as np

x=[0,3]
y=[0,8]

fig,ax=plt.subplots()
ax.arrow(2,1,3,5,head_width=0.1,head_length=0.3,color='black')
ax.scatter(x=2,y=1,color='black')
plt.show()