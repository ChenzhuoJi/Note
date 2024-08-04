a=[1,2,3,4,5,6,7,8,9,]
def exchange(ls,a,b):
    ci=ls[a]
    ls[a]=ls[b]
    ls[b]=ci
    return(ls)
for i in range(0,9):
    for b in range(1,9):
        a0=a[:]
        ls0=exchange(a0,i,b)
        print(ls0)