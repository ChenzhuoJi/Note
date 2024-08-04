a=12312312
b=21321312
if a<b:
    c=b
    b=a
    a=c
x=a
y=b
print(a)
print(b)

s_numbers=[]
#Greatest commen divisor
while a%b!=0:
    c=b
    b=a%b
    a=c
    s_numbers.append(b)
print(s_numbers)

c=b
print(f'gcd(a,b)={c}')
#Least commen mutiple
d=x*y/c
print(f'lcm(a,b)={d}')

