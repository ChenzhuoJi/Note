import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split
from scipy.stats import pearsonr

from Labsta import drawliner
I=[6.500,5.200,5.600,4.500,4.100,3.750,3.000,7.400]
I=np.array(I)
I=I/1000
U=[0.72,0.57,0.62,0.50,0.46,0.418,0.322,0.84]
drawliner(I,U,style=1)
plt.xlabel("I/A",fontsize=12)
plt.ylabel("U/V",fontsize=12)
plt.title("I-U",fontsize=12)
plt.show()

"""
I2=np.array([5.35,7.20,8.15,9.35,3.20,1.76,1.30,0.90])
I2=I2/1000
U2=[0.78,0.90,0.962,1.04,0.6,0.46,0.4,0.34]
drawliner(I2,U2,model=0,style=1)
plt.xlabel("I/A",fontsize=12)
plt.ylabel("U/V",fontsize=12)
plt.title("I-U PN-positive",fontsize=12)
plt.show()"""

"""I3=np.array([4.35,4.45,4.50,3.75,3.80,4.70,4.80,4.15,3.95])
I3=I3/1000000
U3=np.array([0.88,0.96,1.002,0.40,0.44,1.34,1.48,0.730,0.520])
drawliner(I3,U3,style=1,model=0)
plt.xlabel("I/A",fontsize=12)
plt.ylabel("U/V",fontsize=12)
plt.title("I-U,PN-negative",fontsize=12)
plt.show()"""