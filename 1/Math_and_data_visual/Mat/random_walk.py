from random import choice
class RandomWalk:
    """一个可以生成随机数据的类"""
    def __init__(self,num_points=50_000) -> None:
        """初始化随机游走的属性"""
        self.num_points=num_points
        self.x_value=[0]
        self.y_value=[0]
    
    def fill_walk(self):
        """计算随机游走包含的所有点"""

        #不断游走，直到列表大师到指定长度
        while len(self.x_value)<self.num_points:
            x_direction=choice([1,-1])
            x_distance=choice([0,500,1,2])
            x_step=x_direction*x_distance
            
            y_direction=choice([1,])
            y_distance=choice([0,1,2,3,4])
            y_step=y_direction*y_distance
            
            if x_step==0 and y_step==0:
                continue
            x=self.x_value[-1]+x_step
            y=self.y_value[-1]+y_step
            
            self.x_value.append(x)
            self.y_value.append(y)