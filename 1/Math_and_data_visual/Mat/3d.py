import numpy as np  
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  
  
# 创建数据  
x = np.linspace(-5, 5, 100)  
y = np.linspace(-5, 5, 100)  
z = np.sin(np.sqrt(x**2 + y**2))  

# 创建3D图形对象  
fig = plt.figure()  
ax = fig.add_subplot(111, projection='3d')  

# 绘制3D曲面图  
ax.plot_surface(x, y, z, cmap='viridis')  
  
# 添加坐标轴标签  
ax.set_xlabel('X')  
ax.set_ylabel('Y')  
ax.set_zlabel('Z')  
  
# 显示图形  
plt.show()