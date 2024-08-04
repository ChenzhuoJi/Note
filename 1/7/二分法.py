a=-1
b=0
current_n=[]
while b-a>=0.000000001:
    c=(a+b)/2
    current_n.append(c)
    if c**3+c+1==0:
        a=c
    else:
        b=c
print(current_n)
print(len(current_n))
