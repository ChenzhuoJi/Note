sqr=[]
sqr2=[]
for a in range(1,10001):
    sqr.append(a**2)
for a in sqr:
    sqr2.append(2*a)
for a in sqr:
    for b in sqr2:
        if a-b==1:
            print(a,b)
print(sqr)
print(sqr2)