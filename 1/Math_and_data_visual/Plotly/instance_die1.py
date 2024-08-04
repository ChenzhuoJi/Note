from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline


# 创建一个六面的骰子
die = Die()

# 投几次，并将结果保存到列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    # 将result值添加到列表的末尾
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    # 分点数计数
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
# 转换数据的结构
x_values = list(range(1, die.num_sides+1))  # 1-6的列表
data = [Bar(x=x_values, y=frequencies)]
# 设置坐标轴标签
x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}
# 返回指定的图像布局和配置对象
my_layout = Layout(title='投掷1000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
# 生成图表
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')