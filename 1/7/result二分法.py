a=-1
b=0
current_n=[]
c=(a+b)/2
while c**3+c+1>=0.001 or (c**3+c+1)*(-1)>=0.001:
    c=(a+b)/2
    current_n.append(c)
    if c**3+c+1==0:
        a=c
    else:
        b=c
print(c)
print(len(current_n))
#跑不动