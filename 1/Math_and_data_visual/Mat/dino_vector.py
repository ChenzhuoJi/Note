import matplotlib
from vector_drawing import *
def add(v1,v2):
    return(v1[0]+v2[0],v1[1]+v2[1])

dino_vectors=[(6,4),(3,1),(1,2),(-1,5),(-2,5),(-3,4),(4,4),(-5,1),(-5,2),(-5,3),(-4,4),(-3,4),(-2,1),(-2,2),(3,-1),(5,1),(6,4),(2,-3),(2,-4),(0,-3),(-1,-4)]
dino_vectors2=[add((-1.5,2.5),v) for v in dino_vectors]
a=add((-1.5,2.5),(1,3))
print(a)
draw(Points(*dino_vectors),
     Polygon(*dino_vectors))
