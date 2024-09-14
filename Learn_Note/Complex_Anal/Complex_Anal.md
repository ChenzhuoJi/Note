## 复数

$\displaystyle e^{i\theta}=\sum_{n=1}^{\infty}\frac{1}{n!(i\theta)^n}=\cos i\theta+i\sin i\theta$
$\omega^n=z_0=r_0e^{i\theta_0}\implies \omega=r_0^{\frac{1}{n}}e^{(\theta_0+2k\pi)i\setminus n}$

### 拓扑

1. 开集
2. 闭集
3. 连通与连通的开集（称作开域）
4. E的聚点（去心后的周围总有E的点）
5. 导集：全部聚点的集合。
6. 边界点（不去心的周围总有E的点）

**扩充复平面**

## 解析函数
### 复函数
扩展到复数域的函数。
### 极限和连续
总结可得：复函数的极限四则运算性质和实函数一模一样，连续函数的四则运算，以及复合也不改变复函数的连续性

### 导数
$$
\lim_{z \to z_0}\frac{f(z)-f(z_0)}{z-z_0}=f'(z_0), z\in \mathbb{C}
$$
**定理** 
* $(z^n)'=nz^{n-1}$
* 四则运算，以及复合函数求导和实函数性质一样，且可导性可以推出连续性

### Cauchy-Riemman 方程 (_C-R equation_)
我们考虑$f(z)=u(x,y)+iv(x,y)$，也就是实部和虚部时互不决定的二元函数。

**Theorem 2.4.1** ***可导的必要条件***

$u,v$的一阶偏导数存在，并且在该点出有 _C-R equation_ 
$$
\begin{cases}
 u_x(x_0,y_0)=v_y(x_0,y_0) \\
 u_y(x_0,y_0)=-v_y(x_0,y_0) \\
 f'(z_0)=u_x(x_0,y_0)+iv_x(x_0,y_0)  
 \end{cases}
$$

**Theorem 2.4.2** ***可导的充要条件***  

$f(z)=u(x,y)+iv(x,y)$定义在开域上，$f(z)$在$z_0$处可导的充要条件时$u,v$可微且该点满足*C-R equation*

**必要性：** 

**充分性：**

### 解析函数
**Definition :** $f$在$z_0$的一个领域中每点可导，则称$f$在$z_0$解析，若给有一个区域$D$满足$f(z)$解析，则记作$f\in H(D)$

**Theorem 2.5.1** 两个解析函数四则运算或者复合之后之后仍然是解析的

**Theorem 2.5.2** 导数为零的解析函数为常函数

**Theorem 2.5.3** 当$f(z)$解析时，$\displaystyle \frac{\partial f}{\partial \bar{z}}=0\Leftrightarrow \text{C-R equation}$

设$f(x,y)$中：$z=x+iy,\bar{z}=x-iy$ 
$$
x=\frac{1}{2}(z+\bar{z}),y=-\frac{i}{2}(z-\bar{z})
$$
$$
\displaystyle \frac{\partial f}{\partial z}=\frac{\partial f}{\partial x}\frac{\partial x}{\partial z}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial z}
$$
