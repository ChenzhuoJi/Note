from random import randint
class Die:
    """表示一个骰子的类"""
    def __init__(self,num_sides=6):
        """骰子是六面的"""
        self.num_sides=num_sides
    def roll(self):
        """return a randint in (1,num_sides)"""
        return randint(1,self.num_sides)
    