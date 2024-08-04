import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split
from scipy.stats import pearsonr

def drawliner(X,Y,style=0,model=1,scl='blue',pcl='blue',s_size=20):
    """Enter two groups of numbers.Then draw thier association picture on the screen. 
       model可选0和1,0代表不画线性回归曲线,1代表画,默认值为1
       x,y轴标签需要自己设置。"""
    X=np.array(X)
    Y=np.array(Y)
    x=X.reshape(-1,1)
    y=Y.reshape(-1,1)
    if model==1:
        #创建一个线性回归模型
        linearmodel=LinearRegression()
        linearmodel.fit(x,y)
        
        #获取线性回归的斜率和截距
        slope = linearmodel.coef_[0][0]  #斜率
        intercept = linearmodel.intercept_[0] #截距
        print(f"y={slope}x+({intercept})")
        
        #皮尔孙系数
        correlation, p_value = pearsonr(X,Y)
        print(f"回归系数为{correlation}")
        
        #绘制
        x_plot = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)  
        y_plot = slope * x_plot + intercept 
        plt.plot(x_plot,y_plot,color='red')
    
    if style==1:
        plt.scatter(x,y,color=scl,s=s_size,label="Data")
    elif style==2:
        plt.plot(x,y,color=pcl,label="Data line")
    elif style==3:
        plt.scatter(x,y,color=scl,s=s_size,label="Data")
        plt.plot(x,y,color=pcl,label="Data line")
    else:
        print("格式只有\n1:scatter'\n2:'plot'\n3:'plot and scatter'三种选择.")

