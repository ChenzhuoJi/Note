class Car:
    """模拟汽车尝试"""
    
    def __init__(self,make,model):
        self.make=make
        self.modle=model
        self.year=20
        
        '--snip--'
        self.odometer_reading=0
        
    def get_describe_name(self):
        long_name=f"{self.year} {self.make} {self.modle}"
        return long_name.title()
    
    def updated_odometer(self,mileage):
        self.odometer_reading=mileage
        '--snip--'
    def increasement_odometer(self,mile):
        self.odometer_reading+=mile
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it')
        
"------------------snip-------------------"        
class ElectricCar(Car):
    """电动车的独到之处"""
    def __init__(self,make,model):
        """
        先初始化父类的属性，
        再初始化电动汽车特有的属性
        """
        super().__init__(make,model)
        self.battery_size=40
        self.year=100
        
    def describe_battery(self):
        """打印一条描述电池容量的信息"""
        print(f'This car has a {self.battery_size}-kWh battery')
        
        
class Battery:
    
    def __init__(self, battery_size=40):
        """初始化电池数据"""
        self.battery=battery_size 
        
my_new_car=Car('audi','a4',)
#print(my_new_car.get_describe_name())
#my_new_car.updated_odometer(23411)
#my_new_car.increasement_odometer(41132)
#my_new_car.read_odometer()
my_leaf=ElectricCar('nissan','leaf')
print(my_leaf.get_describe_name())
                    