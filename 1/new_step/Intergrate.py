#求积分
import sympy as sy
import numpy as np
import scipy as sc
x=sy.Symbol('x')
n=input('分母多项式最高次是：')
for i in range(n):
    ai=input("第i项的系数为")
    s="a{i}={}"
    
