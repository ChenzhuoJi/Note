import matplotlib.pyplot as plt
import numpy as np
'''x=np.linspace(0,5,200)
y=x/(1-x**2)
plt.figure(num=3,figsize=(8,5))
#figure设置窗口实现
#plot进行绘制，x,y轴，颜色，线宽'''
def draw_pct(x,y):
    plt.plot(x,y,color='red',linewidth=1.0)
    #设置x,y axis lim,and lable
    plt.xlabel('I am x')
    plt.ylabel("I am y")
    plt.show()

def connect(*coordinates,line_color='blue',scatter_color='blue',size=10,):
    ''''connect all coordinates
    not definite the lables,'''
    x,y=[],[]
    a=zip(coordinates)
    for coordinate in list(coordinates):
        x.append(coordinate[0])
        y.append(coordinate[1])
    fig,ax=plt.subplots()
    ax.plot(x,y,color=line_color)
    ax.scatter(x,y,color=scatter_color,s=size)    
    

#将坐标裂开，即对于坐标(x1,y1),(x2,y2),...,(xi,yi)将坐标裂成X(所有的x values),Y(all y values)
def get_value(*coordinates):
    x,y=[],[]
    a=zip(coordinates)
    for coordinate in list(coordinates):
        x.append(coordinate[0])
        y.append(coordinate[1])
    return(x,y)
#将X,Y以坐标的形式压缩进列表
def yield_coordinates(x,y):
    coordinates=[]
    if len(x)==len(y):
        for i in range(len(x)):
            coordinates.append((x[i],y[i]))
        return(coordinates)
    else:
        print('x and y must be equal length')
    
def convolute(a,b):
    '''卷出a,b的积'''
    convolution=[]
    for x in a:
        for y in b:
            convolution.append(x*y)
    #print(convolution)
    return(sum(convolution))

def fgradient(x,y):
    """find gradient,
    找到一个数列的梯度变化,并以数列列表的形式返回"""
    gradients=[]
    def ydifferens(ls):
        """find the difference between numbers in proression"""
        differens=[]
        for i in range(1,len(x)):
            d=ls[i]-ls[i-1]
            differens.append(d)
        return(differens)
    if len(x)==len(y):
        xd=ydifferens(x)
        yd=ydifferens(y)
        for i in range(len(xd)):
            gradient=yd[i]/xd[i]
            gradients.append(gradient)
        #print(gradients)
        return(gradients)
    else:
        print(f'x and y should be equal length')
    

    
        
# a=get_value((1,9),(2,8),(2,9))
# print(a)
# x=a[0]
# y=a[1]
# print(x)
# print(y)
# fig,ax=plt.subplots()
# ax.plot(x,y)
# ax.scatter(x,y)
# plt.show()
# connect((1,9),(2,8),(2,9))
# connect((1,3),(3,2),line_color='red')
# plt.xlabel('hahh')
# plt.show()


#draw cacular
###逼近过程.approximation process
excess_estimates=[]
insufficient_estimates=[]
convolutions=[]
for i in range(2,102):
    xs=np.linspace(0,5,i)
    ys=xs**2
    convolution=convolute(xs,ys)
    dx=5/(i-1)
    excess_estimate=sum(list(dx*ys))
    insufficient_estimate=sum(list(dx*ys[:-1]))
    excess_estimates.append(excess_estimate)
    insufficient_estimates.append(insufficient_estimate)
    convolutions.append(convolution)
x1=range(100)
x2=range(99)    
incr_speed=fgradient(x1,insufficient_estimates)
fig,ax=plt.subplots()
#ax.plot(x1,convolutions,color=(0.2,0.7,0.4))
ax.plot(x1,excess_estimates,color=(0.7,0.2,0.4))
ax.plot(x1,insufficient_estimates,color=(0.4,0.7,0.2))
ax.plot(x2,incr_speed,color='blue')
plt.show()


