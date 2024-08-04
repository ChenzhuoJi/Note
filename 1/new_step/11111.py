import numpy as np
import math
"""def u(S):
    u=math.sqrt(1.1*1.1*(0.001*0.001)+0.1*0.1*(0.001*0.001)+0.0005*0.0005+(1/S)*(1/S))
    return(u)
    
def p(uR,R,d,h):
    ud=0.00577
    y=math.sqrt((uR/R)**2+(2*ud/d)**2+(0.017/40)**2)
    p=h*y
    return(p)

d1=[4.969 ,4.961, 4.959, 4.955, 4.951]
d2=[4.919,4.915,4.911,4.909,4.910]
d3=[4.961,4.955,4.955,4.955,4.956]
arr1=np.array(d1)
arr2=np.array(d2)
arr3=np.array(d3)
v1=np.var(arr1)
v2=np.var(arr2)
v3=np.var(arr3)
a=np.average(arr1)
b=np.average(arr2)
c=np.average(arr3)
s1=v1/math.sqrt(5)
print(s1)
print(a)
print(v2)
print(b)
print(v3)
print(c)
print(u(3370))
print(u(5800))
m1=p(0.000614,0.35,4.959,1.738)
m2=p(0.000996,0.83,4.913,3.927)
m3=p(0.0174,14.8,4.956,1.41)
print(m1,m2,m3)"""
def p(A,d):
    p=(A*A-d*d)/(4*A)
    return(p)
A1=[25.40,30,34.4]
A2=[92.4,102.4,112.4]
d1=[32.9,39.35,50.4]
d2=[8.5,13.8,19.4]
a=[]
b=[]
for i in range(3):
    y=p(A1[i],d2[i])
    a.append(y)
    z=p(A2[i],d1[i])
    b.append(z)
print(a,b)
arr1=np.array(a)
arr2=np.array(b)
c=np.average(arr1)
d=np.average(arr2)
print(c,d)
A3=[20.17,21.82,22.45]
arr3=np.array(A3)
f=np.std(arr3)

print(f)