class Die:
    def __init__(self):
        
        self.sides=6
        
    def roll_die(self):
        from random import randint
        current_number=1
        numbers=[]
        while current_number<=10:
            a=randint(1,self.sides)
            current_number+=1
            numbers.append(a)
        print(numbers)
        
my_dice=Die()
my_dice.sides=50
my_dice.roll_die()