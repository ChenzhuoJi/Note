import numpy as np  
import pandas as pd  
import math
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split  
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
 
sqT=[0.7,0.82825117,0.989949494,1.128716085,1.252198067,1.4]
lambdda=[28.4,33,38.58,44,48.5,51.5]
SqT=np.array(sqT)
Lambda=np.array(lambdda)/100
X = Lambda.reshape(-1, 1)  
y =SqT.reshape(-1, 1)

"""# 创建并拟合线性回归模型  
model = LinearRegression()  
model.fit(X, y)  

# 获取模型的系数（斜率）和截距  
slope = model.coef_[0][0]  
intercept = model.intercept_[0]
print(slope)
print(intercept)

# 计算Pearson相关系数和p-值  
correlation, p_value = pearsonr(SqT,Lambda)  

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
plt.title('Linear Regression of ) Lambda vs T^(1/2) ',fontsize=12)  
plt.xlabel('Lambda',fontsize=12)  
plt.ylabel('T^(1/2)',fontsize=12)  
  
# 显示图例  
plt.legend()
  
# 显示图形  
plt.show()"""

#定义一个函数，让他满足一些shiyan需求
def lab(X,y,):
    model = LinearRegression()  
    model.fit(X, y)  

    # 获取模型的系数（斜率）和截距  
    slope = model.coef_[0][0]  
    intercept = model.intercept_[0]
    print(slope)
    print(intercept)
    print(f"y={slope}x+({intercept})")
    # 计算Pearson相关系数和p-值  
    correlation, p_value = pearsonr(SqT,Lambda)  

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
    plt.title('Linear Regression of ) Lambda vs T^(1/2) ',fontsize=12)  
    plt.ylabel('Lambda(m)',fontsize=12)  
    plt.xlabel('T^(1/2)(N^(1/2))',fontsize=12)  
    
    # 显示图例  
    plt.legend()
    
    # 显示图形  
    plt.show()
    
def sqrtsqur(A):
    sqttsqur=math.sqrt()
lab(y,X)