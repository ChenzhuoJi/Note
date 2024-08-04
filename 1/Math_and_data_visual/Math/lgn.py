import matplotlib.pyplot as plt
import math

#该程序要绘制lgn的求和级数数列的图像
#点数五十
sub=101
n=list(range(1,sub))
an=[]
for i in n:
    lgn=math.log10(i)
    an.append(lgn)
def add(lst,i,j):
    """对列表中的一组求和,从第i项到j项,保证i<j"""
    #注意该函数的列表index从1开始
    if i>j:
        print("请注意首末项大小")
    h=i
    s=0
    while h<=j:
       s+=lst[h-1] 
       h+=1
    return(s)

""" for i in range(1,sub-1):
    m=suml(an,0,i)
    Y.append(m)
Y.insert(0,an[0])
x1=range(1,100)
fig,ax=plt.subplots()
#ax.plot(x1,convolutions,color=(0.2,0.7,0.4))
ax.plot(n,Y,color=(0.7,0.2,0.4))
ax.plot(x1,fgradient(n,Y),color=(0.2,0.4,0.7))
plt.show() """
sub=100#
h1=list(range(1,sub+1))#h的长度为sub
h2=[]
sumh2s=[]
#创建一个从1到100的数表

for i in h1:
    j=math.sqrt(i)
    h2.append(1/j)
for j in range(1,sub+1):
    sumh2=add(h2,1,j)-2*math.sqrt(j)
    
    





