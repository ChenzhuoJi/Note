a=input("被除式多项式的最高次是：")
b=input("除式的最高次是：")
i=0
dd=[]
ds=[]
while i<=int(a):
    c=input(f"被除式{int(a)-i}次项的系数为：")
    i=i+1
    dd.append(int(c))
while i<=int(b):
    c=input(f"除式{int(b)-i}次项的系数为：")
    i=i+1
    ds.append(int(b))
m0=dd[0]/ds[0]
ds1=[]
for i in ds:
    i=i/m0
    ds1.append(i)
dd1=[]
for i in range(int(b)+1):
    c=dd[i]-ds1[i]
    dd1.append[c]
    
#待改进