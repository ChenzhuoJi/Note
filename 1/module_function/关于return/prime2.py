import time
from math import sqrt
start=time.perf_counter()
def Find(list,x):
    for i,item in enumerate(list):
        if item ==x:
            return i

def find_prime(n):
    Num=list(range(2,n))
    for a in Num[:int(sqrt(n))]:
        for b in Num[:]:
            if  b%a==0 and b>a:
                Num.remove(b)
    return (Num)
sss=find_prime(100000)
print(sss)
end=time.perf_counter()
print("run_time",end-start)
