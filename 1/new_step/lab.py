#灵敏度S
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split  
import matplotlib.pyplot as plt
from scipy.stats import pearsonr  
E=[3.5,3.0,2.5,2.0,1.5,1.0,0.5]
I1=[-0.3,-0.5,-0.5,-0.3,-0.2,-0.1,-0.1]
I2=[-16.1,-13.1,-8.4,-6.2,-4.8,-2.4,-1.4]
DI=[]
S=[]
for i in range(len(I1)):
    di=I1[i]-I2[i]
    DI.append(di)
for i in DI:
    s=(1200*i)*0.000001
    S.append(s)
print(DI)
print(S)
E=np.array(E)
S=np.array(S)
X = E.reshape(-1, 1)  
y =S.reshape(-1, 1)  

# 创建并拟合线性回归模型  
model = LinearRegression()  
model.fit(X, y)  

# 获取模型的系数（斜率）和截距  
slope = model.coef_[0][0]  
intercept = model.intercept_[0]
print(slope)
print(intercept)

# 计算Pearson相关系数和p-值  
correlation, p_value = pearsonr(E,S)  

# 打印结果  
print(f"Pearson相关系数: {correlation}")  
print(f"p-值: {p_value}")

# 创建用于绘制拟合线的X值范围  
X_plot = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)  
y_plot = slope * X_plot + intercept  

# 使用matplotlib绘制数据点和拟合线  
plt.scatter(X, y, color='blue',label='Data')  
plt.plot(X_plot, y_plot, color='red', linewidth=2, label='Linear Regression')  

# 添加标题和轴标签  
plt.title('Linear Regression of E vs S',fontsize=16)  
plt.xlabel('E/V',fontsize=16)  
plt.ylabel('S/mA',fontsize=16)  

# 显示图例  
plt.legend()

# 显示图形  
plt.show()