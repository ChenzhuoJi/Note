from math import *
x=1+2j
y=3-2j
# 在Python中，可以使用matplotlib库来绘制向量图形。以下是一个简单的示例代码：

# python
import numpy as np
import matplotlib.pyplot as plt

# 定义向量
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# 绘制向量图形
plt.quiver(x, y,1,0.2)

# 设置坐标轴范围
plt.xlim(-1, 6)
plt.ylim(-1, 11)

# 显示图形
plt.show()

