# 第十四章：数项级数
***
*2024/9/2*
### 数列极限（回忆）

**数列$S_n$的极限定义（$\varepsilon-N$）**：
$\exists S > 0,\forall \varepsilon > 0, \exists N > 0$,使得当$n > N $时，有$|S_n - S| < \varepsilon$,则称${S_n}$收敛。
**单调收敛定理**: 单调有界数列收敛。
**柯西收敛定理**: $S_n$收敛当且仅当：
$\forall \varepsilon > 0, \exists N > 0$,使得当$n > N$ 时，有$|S_{n+m} - S_n| < \varepsilon$,则称$S_n$收敛。
**数列的上下极限**：$\overline{\lim\limits_{n \to \infty}}S_{n} = a$，当且仅当：
1. 存在${m_k}$，使得$\lim\limits_{k \to \infty}S_{m_k} = a$
2. 对任意收敛子列${S_{n_k}}$，$\lim\limits_{k \to \infty}S_{m_k} \le a$
### 级数收敛性的概念和基本性质

**定义：**设$\sum \limits_ {n = 1} ^ \infty u_n$是一个级数，称$u_n$为级数的**通项**。令
$$S_n = \sum \limits_ {k = 1} ^ n u_k = u_1 + u_2 + \cdots + u_n, \qquad n = 1,2,\cdots,$$
称$S_n$为级数$\sum \limits_ {n = 1} ^ \infty u_n$的第n个**部分和**，并称数列${S_n}$为级数$\sum \limits_ {n = 1} ^ \infty u_n$的**部分和数列**。

**定义(级数收敛与发散)：** 如果$\{S_n\}$收敛（到$S$)，则称 $\sum \limits_ {n = 1} ^ \infty u_n$收敛（到$S$)，记为：
$$S = \lim _ {n \to \infty} S_n  = \sum \limits_ {n = 1} ^ \infty u_n$$

如果$\{S_n\}$发散，则称 $\sum \limits_ {n = 1} ^ \infty u_n$发散，
若$\lim \limits_ {n \to \infty} S_n = + \infty(- \infty)$,则记$\sum \limits_ {n = 1} ^ \infty u_n = + \infty(- \infty)$。


**定义(正向级数)：** 若对任意的$n \ge 1,u_n \ge 0$，则称$\sum \limits_ {n = 1} ^ \infty u_n $是**正向级数**。

**例1**： 考虑$\sum \limits_ {n = 1} ^ \infty \frac{1}{n^2} $的收敛性：
**思路**： $$S_n = \sum \limits_ {k = 1} ^ n \frac{1}{k^2} = 1 + \sum \limits_ {k = 2} ^ n \frac{1}{(k -1)k} \le 2 - \frac{1}{n} < 2$$

值得注意的是，该数项级数的值为：
$$\sum \limits_ {n = 1} ^ \infty \frac{1}{n^2}  = \frac{\pi^2}{6}$$
我们将在后续课程进行证明。
**例2**：考虑 $\sum \limits_ {n = 1} ^ \infty \frac{1}{n} $的收敛性：
**思路**：证明 $\sum \limits_ {k = 1} ^ n \frac{1}{n}$无界。值得一提的是，$\sum \limits_ {n = 1} ^ \infty \frac{1}{n} \approx \ln n+r$

$$\sum \limits_ {k = 2^m + 1} ^ {2^{m+1}} \frac{1}{n}  \ge \sum \limits_ {k = 2^m + 1} ^ {2^{m+1}} \frac{1}{2^{m+1}} \ge \frac{1}{2}$$
发散。
**重点：部分和数列无界即发散，对于正向级数，有界即收敛。**


**定理（柯西收敛原理）**：$\sum \limits_ {n = 1} ^ \infty u_n $收敛当且仅当：
$\forall \varepsilon > 0, \exists N > 0$,使得当$n \ge N$ 时，有$|\sum \limits_ {k = n+1} ^ {n+m} u_k| < \varepsilon, \quad \forall\  m \ge 1。$
在上述式子，令$m = 1$，可知$u_n \to 0$，由此得到下述定理：
**级数收敛的必要条件：**
若$\sum \limits_ {n = 1} ^ \infty u_n $收敛，则$\lim\limits_{n\to \infty}u_n = 0$。
**控制收敛定理**：
设对$n \ge 1,|u_n| \le v_n$，如果$\sum \limits_ {n = 1} ^ \infty u_n $收敛，则$\sum \limits_ {n = 1} ^ \infty u_n $也收敛。
**证明：** 由$\sum \limits_ {n = 1} ^ \infty v_n $收敛，应用柯西收敛原理，有：
$\forall \varepsilon > 0, \exists N > 0$,使得当$n \ge N$ 时，有$v_{n+1} + v_{n+2} + \cdots + v_{n+m}  < \varepsilon , \quad \forall\  m \ge 1。$于是：
$$|u_{n+1} + u_{n+2} + \cdots + u_{n+m} | < \varepsilon$$由柯西收敛原理可知，$\sum \limits_ {n = 1} ^ \infty u_n $收敛。
**例3：** 考虑$\sum \limits_ {n = 1} ^ \infty \frac{\sin \sqrt{n}}{n^2} $的收敛性：
思路：$\frac{\sin \sqrt{n}}{n^2} \le \frac{1}{n^2} $，收敛。
**例4：**：考虑$\sum \limits_ {n = 1} ^ \infty q^n $的收敛性：
$$\begin{align}
\begin{aligned}
    S_n = \sum \limits_ {k = 1} ^ \infty q^k = \{n+1,\quad q = 1\\
    \end{aligned}
\end{align}$$


**级数的四则运算：** 若$\sum \limits_ {n = 1} ^ \infty u_n ,\sum \limits_ {n = 1} ^ \infty u_n $收敛,则：

* $\sum \limits_ {n = 1} ^ \infty (u_n + v_n) = \sum \limits_ {n = 1} ^ \infty u_n + \sum \limits_ {n = 1} ^ \infty v_n$
* $\sum \limits_ {n = 1} ^ \infty C u_n  = C \sum \limits_ {n = 1} ^ \infty u_n $
* $\sum \limits_ {n = 1} ^ \infty v_n u_n  = \sum \limits_ {n = 1} ^ \infty v_n \sum \limits_ {n = 1} ^ \infty u_n ?$后续课程将对此进行说明。

和数列极限类似，我们**更关注**$\sum \limits_ {n = N+1} ^ \infty u_n $的收敛性，即只关注后续无穷项是否能控制，而对前几项不很关心。


### 正项级数

**例1**：考虑$\sum \limits_ {n = 1} ^ \infty \frac{1}{n^p} $的收敛性：

$$\begin{align}
\begin{aligned}
    &p > 2,&\frac{1}{n^p} < \frac{1}{n^2}，收敛\\
    &0< p < 1,&\frac{1}{n^p} \ge \frac{1}{n}，发散\\
    \end{aligned}
\end{align}$$

当$1<p<2$时，令$f(x) = \frac{1}{x^p}$，考虑:$$\int \limits_1 ^ n f(x)\ {\rm{d}}x = \frac{n^{1-p}}{1-p} - \frac{1}{1-p}$$


**定理**：设$f(x)$在$[1,+\infty)$上非负递减，令
$$A_n =\int \limits_1 ^ n f(x)\ {\rm{d}}x  $$
则$\sum \limits_ {n =1} ^ \infty f(n) $与$\{A_n\}$同时收敛，同时发散。

**例2：** 考虑$\sum \limits_ {n = 3} ^ \infty \frac{1}{n(\ln n) ^ p} $的收敛性：
思路： $$A_n =\int \limits_3 ^ n \frac{1}{x(\ln x) ^ p}\ {\rm{d}}x =\int \limits_3 ^ n \frac{\rm{d}\ln x}{(\ln x)^p}=\left.\frac{1}{-p+1} (\ln x)^{-p+1}\right |_3 ^n $$
上述级数显然是收敛的.

***