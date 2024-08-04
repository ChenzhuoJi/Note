import numpy as np  
import pandas as pd  
import math
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split  
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

t=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
Te=[39.6,36.4,35.2,31.3,28.6,27.6,26.3,25.6,25.3,25.0,24.8,24.8,24.8,24.8,24.8,24.8]
RoomTe=[27.1,27.1,27.1,27.1,27.1,27.1,27.1,27.1,27.1,27.1,27.1,27.1,27.1,27.1,27.1,27.1]
t=np.array(t)
Te=np.array(Te)
X = t.reshape(-1, 1)  
Y =Te.reshape(-1, 1)  

# 使用matplotlib绘制数据点和拟合线  
plt.plot(X, Y, color='blue')  
plt.scatter(X,Y,color='black')
plt.plot(X,RoomTe,color='red')
plt.scatter(X,RoomTe,color='black')
# 添加标题和轴标签  
plt.title("Tempreture vs Time",fontsize=16)  
plt.xlabel('t/s',fontsize=16)  
plt.ylabel('T/°C',fontsize=16)  

# 使用fill_between函数填充y下方的区域（即y与x轴之间的区域）  
plt.fill_between(t, 27.1, Te, color='blue', alpha=0.5)  # 0是基线，y是上面的曲线

# 显示图例  
plt.legend()

# 显示图形  
plt.show()

