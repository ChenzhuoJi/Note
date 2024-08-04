import numpy as np
import plotly.graph_objects as go

x = np.arange(5)
y1 = np.random.rand(5) * 5
y2 = np.random.rand(5) * 5
y3 = np.random.rand(5) * 5

fig = go.Figure(
    data=[
        # name为图例名，textfont设置字体属性，mode为绘图模式，marker设置颜色否则后续导出图像会丢失颜色（不导出可不设置该参数也有默认颜色）
        go.Scatter(name='Lines', x=x, y=y1, textfont=dict(size=25), mode='lines', marker=dict(color='#0068C9')),
        go.Scatter(name='Markers', x=x, y=y2, textfont=dict(size=25), mode='markers'),
        go.Scatter(name='Lines&Markers', x=x, y=y3, textfont=dict(size=25), mode='lines+markers'),
    ]
)

# 设置图像格式
fig.update_layout(
    autosize=False, width=1200, height=650,  # 取消自动大小，手动设置宽高
    title='This is title',  # 标题
    xaxis=dict(title='X', nticks=5),  # 设置X轴属性
    yaxis=dict(title='Y', nticks=11, range=(0, 5)),  # 设置Y轴属性，nticks表示划分为多少段
    showlegend=True  # 显示图例
)

fig.show()