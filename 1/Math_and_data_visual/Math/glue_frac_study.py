from math import *
import time
s=time.time()
def f(a):
    return(a-int(a))
def d(a,b):
    b=1
    return(b/a)
def g_f(a):
    gcl=[]
    while True:
        b=a
        c=b
        a1=int(b)
        r1=f(b)
        gcl.append(a1)
        b=d(r1)
        
e=time.time()
print(e-s)