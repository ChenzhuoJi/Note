from vector_drawing import *
from math import sqrt
def add(v1,v2):
    return(v1[0]+v2[0],v1[1]+v2[1])
     
def length(v):
    return sqrt(v[0]**2+v[1]**2)

def sca_mul(num,v):
    return(num*v[0],num*v[1])

def dot_pro(v1,v2):
    return(v1[0]*v2[0]+v1[1]*v2[1])