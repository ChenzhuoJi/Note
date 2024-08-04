import matplotlib.pyplot as plt

# 创建一个新的图形
fig, ax = plt.subplots()

# 在坐标(1, 2)处绘制一个箭头，向正x方向延伸3个单位，向正y方向延伸4个单位
ax.arrow(1, 2, 3, 4, head_width=0.05, head_length=0.1, fc='black', ec='black')

# 设置坐标轴的范围
ax.set_xlim([0, 6])
ax.set_ylim([0, 6])

# 显示图形
plt.show()
