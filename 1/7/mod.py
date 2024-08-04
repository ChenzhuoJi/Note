b=333
a=891231

s_numbers=[]
while a%b!=0:
    c=b
    b=a%b
    a=c
    s_numbers.append(b)
print(s_numbers)