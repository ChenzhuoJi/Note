import numpy as np  
import pandas as pd  
import math
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split  
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

m=[0.5,1,1.5,2,2.5,3]
x=[24.33,25.76,27.32,29.17,30.85,32.37]
m=np.array(m)
x=np.array(x)
X=m.reshape(-1,1)
Y=x.reshape(-1,1)
# 创建并拟合线性回归模型  
model = LinearRegression()  
model.fit(X, Y)  

# 获取模型的系数（斜率）和截距  
slope = model.coef_[0][0]  
intercept = model.intercept_[0]
print(slope)
print(intercept)

# 计算Pearson相关系数和p-值  
correlation, p_value = pearsonr(m,x)  

# 打印结果  
print(f"Pearson相关系数: {correlation}")  
print(f"p-值: {p_value}")

# 创建用于绘制拟合线的X值范围  
X_plot = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)  
y_plot = slope * X_plot + intercept  

# 使用matplotlib绘制数据点和拟合线  
plt.scatter(X, Y, color='blue',label='Data')  
plt.plot(X_plot, y_plot, color='red', linewidth=2, label='Linear Regression')  
  
# 添加标题和轴标签  
plt.title('m-x',fontsize=12)  
plt.xlabel('m(g)',fontsize=12)  
plt.ylabel('x(cm)',fontsize=12)  
  
# 显示图例  
plt.legend()
  
# 显示图形  
plt.show()