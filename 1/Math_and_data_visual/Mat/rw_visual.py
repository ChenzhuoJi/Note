import pygame
import matplotlib.pyplot as plt
from random_walk import RandomWalk
symbol=True
while symbol:
    rw=RandomWalk()
    rw.fill_walk()
    plt.style.use('classic')
    fig,ax=plt.subplots(figsize=(15,8))
    point_number1=range(rw.num_points)
    point_number2=range(20001,100000)
    
    ax.scatter(rw.x_value,rw.y_value,c=point_number1,cmap=plt.cm.Greens,
          edgecolors='none',s=5)
    ax.get_xaxis().set_visible(True)
    ax.get_yaxis().set_visible(True)
    
    ax.set_aspect('equal')
    plt.show()
    break
    
        
    