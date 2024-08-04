a=-1
b=0
current_n=[]
aaa=1
while aaa>=0.000000000000000001:
    aaa=aaa/10
    while b-a>=aaa:
        c=(a+b)/2
        current_n.append(c)
    
        if c**3+c+1<=0:
            a=c
        else:
            b=c
    print(len(current_n))
if c**3+c+1<=0.00001:
    print('yes')
else:
    print('no')