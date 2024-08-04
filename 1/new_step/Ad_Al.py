"""在Python中，你可以使用NumPy库来计算矩阵的逆。以下是一个简单的例子：
"""
import numpy as np
from scipy import linalg
import sympy as sp
# 定义一个矩阵
A = np.array([[1, 2], [3, 4]])

# 计算矩阵的逆
A_inv = np.linalg.inv(A)

print("原矩阵 A:")
print(A)

print("矩阵 A 的逆:")
print(A_inv)

"""
注意，不是所有的矩阵都有逆矩阵。如果一个矩阵是奇异的（即它的行列式为零），那么它就没有逆矩阵。在尝试计算逆矩阵之前，
你可能需要检查矩阵是否是奇异的。你可以使用`np.linalg.det()`函数来计算矩阵的行列式，如果行列式为零，那么矩阵就是奇异的，没有逆矩阵。
"""

"""在Python中，计算矩阵的特征值和特征多项式主要依赖于NumPy和SciPy这两个科学计算库。以下是使用这些库计算特征值和特征多项式的方法：

### 使用NumPy

NumPy库提供了`numpy.linalg.eigvals`和`numpy.linalg.eig`函数来计算矩阵的特征值和特征向量。

```python"""


# 定义一个矩阵
A = np.array([[1, 2], [3, 4]])

# 计算特征值
eigenvalues = np.linalg.eigvals(A)
print("特征值:", eigenvalues)

# 计算特征向量
eigenvectors = np.linalg.eig(A)[1]
print("特征向量:", eigenvectors)

# 计算特征多项式
# 特征多项式是 det(A - λI)，其中λ是特征值，I是单位矩阵
# NumPy没有直接计算特征多项式的函数，但可以通过计算行列式得到
# 假设我们想要计算特征值λ=2时的特征多项式值
lambda_value = 2
I = np.eye(A.shape[0])  # 单位矩阵
characteristic_polynomial_value = np.linalg.det(A - lambda_value * I)
print("特征多项式在λ={}时的值:".format(lambda_value), characteristic_polynomial_value)
"""```

### 使用SciPy

SciPy库提供了`scipy.linalg.eigvals`和`scipy.linalg.eig`函数，它们与NumPy中的函数类似，但提供了更多的选项和更好的性能。

```python"""


# 定义一个矩阵
A = np.array([[1, 2], [3, 4]])

# 计算特征值
eigenvalues = linalg.eigvals(A)
print("特征值:", eigenvalues)

# 计算特征向量
eigenvectors = linalg.eig(A)[1]
print("特征向量:", eigenvectors)

# SciPy同样没有直接计算特征多项式的函数，但可以通过计算行列式得到
# 计算特征多项式在λ=2时的值
lambda_value = 2
I = np.eye(A.shape[0])  # 单位矩阵
characteristic_polynomial_value = np.linalg.det(A - lambda_value * I)
print("特征多项式在λ={}时的值:".format(lambda_value), characteristic_polynomial_value)


### 计算完整的特征多项式
"""
如果你想计算完整的特征多项式（即关于λ的多项式），你需要手动进行。这通常是通过计算矩阵的行列式并展开得到的，其中矩阵的元素是原始矩阵元素
与(λ - 原始对角元素)的差值。
"""


# 定义一个矩阵
A = np.array([[1, 2], [3, 4]])

# 定义符号变量λ
lambda_symbol = sp.symbols('lambda')

# 创建符号矩阵
A_sym = sp.Matrix(A)

# 计算特征多项式
characteristic_polynomial = A_sym.charpoly(lambda_symbol)
print("特征多项式:", characteristic_polynomial)


"""在这个例子中，我们使用了SymPy库，它是一个符号计算库，可以处理符号变量并计算多项式。
charpoly方法可以直接计算矩阵的特征多项式。
请注意，对于大型矩阵，计算完整的特征多项式可能会非常耗时，而且结果可能非常复杂。在实际应用中，
通常只关注特征值或特征多项式的某些特定点（如根）的计算。"""


# 计算矩阵的行列式
det_A = np.linalg.det(A)

if det_A == 0:
    print("矩阵 A 是奇异的，没有逆矩阵。")
else:
    A_inv = np.linalg.inv(A)
    print("矩阵 A 的逆:")
    print(A_inv)

"""以上代码会先检查矩阵A是否是奇异的，如果不是，则计算并打印其逆矩阵。如果是奇异的，则打印一条消息说明它没有逆矩阵。"""