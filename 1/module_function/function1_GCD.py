def GCD(a,b):
    #"""输出最大公因数"""
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
GCD(739297,13123)