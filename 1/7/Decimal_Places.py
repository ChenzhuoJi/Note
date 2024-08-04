a=0.0000000001
current_numeber=-1
b=a*10
if b%10==0:
    print('integer')
else:
    while a%10!=0:
        a=a*10
        current_numeber+=1
    print(current_numeber)
    