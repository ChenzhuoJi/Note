import time
start=time.time()
def find_prinme(n):
    Prime=[]
    for a in range(2,n):
        for b in range(2,a):
            if a%b == 0:
                break
        else:
            Prime.append(a)
    return(Prime)
Prime=find_prinme(100000)
print(Prime)
end=time.time()
print(end-start)        
        
        
