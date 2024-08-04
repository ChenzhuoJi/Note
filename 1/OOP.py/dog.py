class Dog:
    """一次模拟小狗的简单尝试"""
    
    def __init__(self,name,age):
        """初始化attribute"""
        self.name=name
        self.age=age
        
    def sit(self):
        """模拟小狗的简单尝试"""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """模拟小狗收到命令"""
        print(f'{self.name} rollde over')
        
my_dog=Dog('Whillie',age=6)
my_dog.sit()
