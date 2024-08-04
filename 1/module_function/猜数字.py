a=520
you_guess=True
while you_guess:
    x=input("x=")
    x=int(x)
    if x<a:
        
        print('猜小了')
    elif x>a:
        
        print('猜大了')
    elif x==a:
        
        you_guess=False
    else:
        print('illegal format')
print('i   love    you ')