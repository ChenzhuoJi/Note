import sympy as sp

"""
EXAMPLE:
SOLVE THE POLYNOMIAL EQUATION

x=sp.symbols("x")
equation=x**5+x-1

a=str(equation)

solutions=sp.solve(equation,x,dict=True)

print(f"{a}的解为：\n")

print(type(solutions))

print(solutions)

THE ANSWER:
x**5 + x - 1的解为:

<class 'list'>

[
{x: 1/2 - sqrt(3)*I/2}, 
{x: 1/2 + sqrt(3)*I/2}, 
{x: -1/3 + (-1/2 - sqrt(3)*I/2)*(sqrt(69)/18 + 25/54)**(1/3) + 1/(9*(-1/2 - sqrt(3)*I/2)*(sqrt(69)/18 + 25/54)**(1/3))}, 
{x: -1/3 + 1/(9*(-1/2 + sqrt(3)*I/2)*(sqrt(69)/18 + 25/54)**(1/3)) + (-1/2 + sqrt(3)*I/2)*(sqrt(69)/18 + 25/54)**(1/3)}, 
{x: -1/3 + 1/(9*(sqrt(69)/18 + 25/54)**(1/3)) + (sqrt(69)/18 + 25/54)**(1/3)}#REAL SL
]
"""

"""
x=sp.symbols("x")
poly=x**4-1
factors=sp.factor(poly)
print(factors)
"""#只能分解成有理式

#改进
"""
x=sp.symbols("x")
poly=x**4-1

roots=[]
solutions=sp.solve(poly,x,dict=True)
rootsnumber=len(solutions)
for i in range(rootsnumber):
    root=solutions[i][x]
    roots.append(root)
   
#循环结构写出最后多项式
i=1   
factors=x-roots[0]
while i<rootsnumber:
    factors=factors*(x-roots[i])
    i=i+1
print(factors)

ANWSER:
(x - 1)*(x + 1)*(x - I)*(x + I)

"""
#写成函数
def Factor(polynomial):
    #求根
    x=sp.symbols("x")
    poly=polynomial
    
    roots=[]
    solutions=sp.solve(poly,x,dict=True)
    rootsnumber=len(solutions)
    for i in range(rootsnumber):
        root=solutions[i][x]
        roots.append(root)
    
    #循环结构写出最后多项式
    i=1   
    factors=x-roots[0]
    while i<rootsnumber:
        factors=factors*(x-roots[i])
        i=i+1
        
    return(factors)


"""
MUTIPLE PLYNOMIALS

RMK:这种乘法最后将多项式展开了

# 定义变量
x = sp.symbols('x')

# 创建多项式
p1 = sp.Poly(x**2 + 2*x + 1)
p2 = sp.Poly(x**2 - x + 1)

# 对多项式进行乘法运算
product = p1 * p2

# 打印结果
print(product)

ANWSER:
Poly(x**4 + x**3 + x + 1, x, domain='ZZ')
"""
x=sp.symbols("x")
poly=x**5+1
factorpoly=Factor(poly)
#print(factorpoly)
solutions=sp.solve(poly,x,dict=True)
#print(f"\n{solutions}")

"""
解为：
[
{x: -1}, 
{x: 1/4 + sqrt(5)/4 + I*sqrt(5/8 - sqrt(5)/8)}, 
{x: -sqrt(5)/4 + 1/4 - sqrt(5)*I*sqrt(5/8 - sqrt(5)/8)/2 - I*sqrt(5/8 - sqrt(5)/8)/2}, 
{x: 1/4 + sqrt(5/8 - sqrt(5)/8)*sqrt(sqrt(5)/8 + 5/8) - sqrt(5)*I*sqrt(sqrt(5)/8 + 5/8)/4 - I*sqrt(sqrt(5)/8 + 5/8)/4 - I*sqrt(5/8 - sqrt(5)/8)/4 + sqrt(5)*I*sqrt(5/8 - sqrt(5)/8)/4}, 
{x: -sqrt(5/8 - sqrt(5)/8)*sqrt(sqrt(5)/8 + 5/8) + 1/4 - I*sqrt(5/8 - sqrt(5)/8)/4 + I*sqrt(sqrt(5)/8 + 5/8)/4 + sqrt(5)*I*sqrt(5/8 - sqrt(5)/8)/4 + sqrt(5)*I*sqrt(sqrt(5)/8 + 5/8)/4}
]
"""

#分解为实多项式