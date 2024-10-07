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

### 初等解析函数

$\displaystyle \sin z=\frac{1}{2i}(e^{iz}-e^{-iz}),\cos z=\frac{1}{2}(e^{iz}+e^{-iz})$
$\displaystyle \sin z=\sin x\ch y+i\cos x\sh y,\sin^2 z=\sin^2 x+\sh^2 y$
$\sin z,\cos z$都是无界的

## Charpter 3 复积分、柯西定理
### 3.1 路径
积分的定义最初是在路径上说的，因为复平面是一个二维的平面，所以探寻一维度上的积分要寻找一个一维指标参数$t$, 由$t$生成一个路径才可以积分。

设$\displaystyle  t\in [a,b]$, 路径定义为$\Gamma=\left\{ z(t):z(t)=x(t)+iy(t),t\in [a,b] \right\} $.

路径的长度可以用实值$t$的积分得到。
$$
|\Gamma|=\sum_{k=1}^{n}\int_{t_{k-1}}^{t_k}|z'(t)| \mathrm{d}t=\sum_{k=1}^{n}\int_{t_{k-1}}^{t_k}\sqrt{[x'(t)]^2+[y'(t)]^2}  \mathrm{d}t
$$

### 复积分
最初的复积分是含参数定义的：
$$
\int_{a}^{b}\omega(t)  \mathrm{d}t=\int_{a}^{b}u(t)  \mathrm{d}t+i\int_{a}^{b}v(t)  \mathrm{d}t
$$
所以线性空间性质和绝对值不等式是显然的,其中绝对值不等式为：
$$
\left| \int_{a}^{b}\omega(t)  \mathrm{d}t \right| \le \int_{a}^{b}|\omega(t)|  \mathrm{d}t
$$

下面我们给出$f(\omega(t))$的积分形式，设$\Gamma:\omega(t)=x(t)+iy(t),t\in [a,b]$，$f(\omega)=u(x,y)+iv(x,y)$是一个复值函数。
$$
\int_{\Gamma}f(\omega)\mathrm{d}\omega=\int_{b}^{a}f(\omega(t))\omega'(t)  \mathrm{d}t=\int_{a}^{b}(ux'-vy')  \mathrm{d}t+i\int_{a}^{b}(vx'+uy')  \mathrm{d}t
$$
线性空间性质和绝对值不等式性质仍然是显然的，特别的:当$|f(z)|\le M$时
$$
\int_{\Gamma}f(z)\mathrm{d}z\le M|\Gamma|
$$

### Cauthy定理
**Theorem 3.3.1** 设$\Gamma$是一条正向的简单闭路径，内部为$D$, $\bar{D}=D\cup \Gamma$, 若由$f\in H(\bar{D})$，则
$$
\int_{\Gamma}f(z)\mathrm{d}z=0
$$

### 单连通和多连通

### 原函数，积分和路径无关
**Def 3.5.1** **原函数**：设$F(z),f(z)$是开域$D$上的两个函数并且对于每一点$z\in D$都有$F'(z)=f(z)$, 则称$F(z)$是$f(z)$在$D$上的一个原函数。