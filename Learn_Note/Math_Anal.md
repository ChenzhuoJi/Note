# 第十四章：数项级数
***
*2024/9/2*
## 数列极限（回忆）

**数列$S_n$的极限定义（$\varepsilon-N$）**：
$\exists S > 0,\forall \varepsilon > 0, \exists N > 0$,使得当$n > N $时，有$|S_n - S| < \varepsilon$,则称${S_n}$收敛。
**单调收敛定理**: 单调有界数列收敛。
**柯西收敛定理**: $S_n$收敛当且仅当：
$\forall \varepsilon > 0, \exists N > 0$,使得当$n > N$ 时，有$|S_{n+m} - S_n| < \varepsilon$,则称$S_n$收敛。
**数列的上下极限**：$\overline{\lim\limits_{n \to \infty}}S_{n} = a$，当且仅当：
1. 存在${m_k}$，使得$\lim\limits_{k \to \infty}S_{m_k} = a$
2. 对任意收敛子列${S_{n_k}}$，$\lim\limits_{k \to \infty}S_{m_k} \le a$
## 14.1级数收敛性的概念和基本性质

**定义：**设$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$是一个级数，称$u_n$为级数的**通项**。令
$$S_n = \sum \limits_ {k = 1} ^ n u_k = u_1 + u_2 + \cdots + u_n, \qquad n = 1,2,\cdots,$$
称$S_n$为级数$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$的第n个**部分和**，并称数列${S_n}$为级数$\sum \limits_ {n = 1} ^ \infty u_n$的**部分和数列**。

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
**例3：** 考虑$\displaystyle\sum \limits_ {n = 1} ^ \infty \frac{\sin \sqrt{n}}{n^2} $的收敛性：
思路：$\displaystyle\frac{\sin \sqrt{n}}{n^2} \le \frac{1}{n^2} $，收敛。
**例4：**：考虑$\displaystyle\sum \limits_ {n = 1} ^ \infty q^n $的收敛性：
$$\begin{align}
\begin{aligned}pip insatll latex2sympy
    S_n = \sum \limits_ {k = 1} ^ \infty q^k = \{n+1,\quad q = 1\\
    \end{aligned}
\end{align}$$


**级数的四则运算：** 若$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n ,\sum \limits_ {n = 1} ^ \infty u_n $收敛,则：

* $\displaystyle\sum \limits_ {n = 1} ^ \infty (u_n + v_n) = \sum \limits_ {n = 1} ^ \infty u_n + \sum \limits_ {n = 1} ^ \infty v_n$
* $\displaystyle\sum \limits_ {n = 1} ^ \infty C u_n  = C \sum \limits_ {n = 1} ^ \infty u_n $
* $\displaystyle\sum \limits_ {n = 1} ^ \infty v_n u_n  = \sum \limits_ {n = 1} ^ \infty v_n \sum \limits_ {n = 1} ^ \infty u_n ?$后续课程将对此进行说明。

和数列极限类似，我们**更关注**$\displaystyle\sum \limits_ {n = N+1} ^ \infty u_n $的收敛性，即只关注后续无穷项是否能控制，而对前几项不很关心。


## 14.2正项级数

**例1**：考虑$\displaystyle\sum \limits_ {n = 1} ^ \infty \frac{1}{n^p} $的收敛性：

$$\begin{align}
\begin{aligned}
    &p > 2,&\frac{1}{n^p} < \frac{1}{n^2}，收敛\\
    &0< p < 1,&\frac{1}{n^p} \ge \frac{1}{n}，发散\\
    \end{aligned}
\end{align}$$

当$1<p<2$时，令$f(x) = \frac{1}{x^p}$，考虑:$$\int \limits_1 ^ n f(x)\ {\rm{d}}x = \frac{n^{1-p}}{1-p} - \frac{1}{1-p}$$


**定理**：设$f(x)$在$[1,+\infty)$上非负递减，令
$$A_n =\int \limits_1 ^ n f(x)\ {\rm{d}}x  $$
则$\displaystyle\sum \limits_ {n =1} ^ \infty f(n) $与$\displaystyle\{A_n\}$同时收敛，同时发散。

**例2：** 考虑$\displaystyle \sum \limits_ {n = 3} ^ \infty \frac{1}{n(\ln n) ^ p} $的收敛性：
思路： $$A_n =\int \limits_3 ^ n \frac{1}{x(\ln x) ^ p}\ {\rm{d}}x =\int \limits_3 ^ n \frac{\rm{d}\ln x}{(\ln x)^p}=\left.\frac{1}{-p+1} (\ln x)^{-p+1}\right |_3 ^n $$
上述级数显然是收敛的.

***
*2024/09/04*

回忆：
对$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$ 与$\displaystyle\sum \limits_ {n = 1} ^ \infty v_n$，若均为正向级数，且$u_n \le v_n$，则二者同时收敛，同时发散。


**定理1:** 设对$ n \ge 1,u_n \ge 0, v_n > 0$,且
$$
\lim _{n \to \infty} \frac{u_n}{v_n} = l \in [0,+\infty)
$$
（1）若$0 < l < + \infty$，则$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$ 与$\displaystyle\sum \limits_ {n = 1} ^ \infty v_n$同时收敛与发散。
（2）若$l = 0$,$\displaystyle\sum \limits_ {n = 1} ^ \infty v_n$收敛，则$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$收敛。
（3）若$l \to + \infty$, $\displaystyle\sum \limits_ {n = 1} ^ \infty v_n$发散，则$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$发散。

证明：
(1)

由$\displaystyle \lim \limits_{n \to \infty} \frac{u_n}{v_n} = l$,对$\displaystyle \varepsilon_0 = \frac{l}{2}$,$\exists N > 0$,使得当$\displaystyle n \ge N$ 时，有$\displaystyle |\frac{u_n} {v_n} - l| \le \varepsilon_0 = \frac{l}{2}$。
即可得到$\displaystyle \frac{1}{2} v_n \le u_n \le \frac{3}{2}v_n$由此可得，$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$ 与$\displaystyle\sum \limits_ {n = 1} ^ \infty v_n$同时收敛与发散。


例1：$\displaystyle\sum \limits_ {n = 2} ^ \infty \frac{1}{n(\sqrt[n]{n} - 1)}$

例2：$\displaystyle\sum \limits_ {n = 1} ^ \infty \sin\frac{x}{n^p}, \quad p > 0$

思路：考虑
$$
\lim _{n \to + \infty} \frac{\sin\frac{x}{n^p}}{\frac{x}{n^p}} = 1
$$


例3：$\displaystyle\sum \limits_ {n = 1} ^ \infty \ [{\rm{e}} - (1 + \frac{1}{n})^n]$

思路:

$$
{\rm{e}} - (1 + \frac{1}{n})^n = {\rm{e}}- \exp(n \ln (1 + \frac{1}{n}))
$$
利用泰勒展开:
$$
{\rm{e}} - \exp(1 - \frac{1}{2n} + o(\frac{1}{n^2})) = \frac{{\rm{e}}}{2n} + o(\frac{1}{n^2})
$$
所以：
$$
\lim _{n \to + \infty} \frac{{\rm{e}} - (1 + \frac{1}{n})^n}{\frac{{\rm{e}}}{2n}} = 1
$$


**定理（柯西判别法）：**

设$\displaystyle n \ge 1, u_n \ge 0, \ r = \overline{\lim \limits_{n \to \infty}} \sqrt[n]{u_n}$。
* 若$r < 1$，则$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$收敛。
*  若$r > 1$，则$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$发散。
*  若$r < 1$，无法判断敛散性。例如$\displaystyle\sum \limits_ {n = 1} ^ \infty \frac{1}{n}$和$\displaystyle\sum \limits_ {n = 1} ^ \infty \frac{1}{n^2}$，前者发散，后者收敛。


**证明：**

（1）由$r = \overline{\lim \limits_{n \to \infty}} \sqrt[n]{u_n} < 1$,知对$r < q < 1$,存在$N$，使得当$n \ge N$ 时，有$\sqrt[n]{u_n} \le q^n$，从而$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$收敛。
（2）$r = \overline{\lim \limits_{n \to \infty}} \sqrt[n]{u_n} > 1$知，存在子列$\displaystyle \{m_k\}$使得$\displaystyle \sqrt[n_k]{u_{n_k}} > 1$，从而$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$发散。
**定理（达朗贝尔判别法）：**
设$\displaystyle n \ge 1, u_n > 0$
* 若$\overline r = \displaystyle \overline{\lim \limits_{n \to \infty}}\frac{u_{n+1}}{u_n} < 1$，则$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$收敛。
* 若$\displaystyle \underline r = \varliminf\limits _{n \to \infty}\frac{u_{n+1}}{u_n} > 1 $则$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$发散。

证明：

（1）由$\overline r = \displaystyle \overline{\lim \limits_{n \to \infty}}\frac{u_{n+1}}{u_n} < 1$，知对$\displaystyle r < 1$，存在$N$，使得当$\displaystyle n \ge N$ 时，有$\displaystyle \frac{u_{n+1}}{u_n}  \le q$
于是：
$$
u_n \le q u _ {n - 1} \le q^2 u _ {n - 2}  \le \cdots \le q^{n - N}u_N
$$
从而$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$收敛。

（2）由$\displaystyle \underline r = \varliminf\limits _{n \to \infty}\frac{u_{n+1}}{u_n} > 1 $，则存在子列$\{n_k\}$使得
$$
u_{n_{kn}} \ge q u _ {n_{k(n-1)}} \ge \cdots \ge q^{kn - kN}u_{kN}。
$$
从而$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$发散。
**例：** 判断$\displaystyle\sum \limits_ {n = 1} ^ \infty n! (\frac{x}{n})^ n, \quad x > 0$的敛散性

**思路：**
$$
\lim_{n \to \infty} \frac{(n+1)! (\frac{x}{n+1})^ {n+1} }{n! (\frac{x}{n})^ n} = \frac{x}{e}
$$
1. 若$x < {\rm{e}}$，则$\displaystyle\sum \limits_ {n = 1} ^ \infty n! (\frac{x}{n})^ n$收敛。
2. 若$x > {\rm{e}}$，则$\displaystyle\sum \limits_ {n = 1} ^ \infty n! (\frac{x}{n})^ n$发散。
3. 若$x = {\rm{e}}$， 所以$\displaystyle\sum \limits_ {n = 1} ^ \infty n! (\frac{x}{n})^ n$发散。

**例：** 判断$\displaystyle\sum \limits_ {n = 1} ^ \infty  \frac{x^n}{(1+x)(1+x)^2\cdots(1+x)^n}, \quad x > 0$的敛散性

**思路：** $$
\frac{u_{n +1}}{u_n} =\frac{x}{1 + x^{n +1} }
$$
所以：
$$
\lim_{x \to + \infty} \frac{x}{1 + x^{n +1} } = 
$$

从而$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$收敛。
**例：** 

可以利用柯西判别法求解。

## 14.4一般项级数

**定理1：** 若$\displaystyle\sum \limits_ {n = 1} ^ \infty 
|u_n|$收敛，则$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$收敛。
**定义1：** 
* 若$\displaystyle\sum \limits_ {n = 1} ^ \infty 
|u_n|$收敛，则称$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$绝对收敛。
* 若$\displaystyle\sum \limits_ {n = 1} ^ \infty 
|u_n|$发散，$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$收敛，则称$\displaystyle\sum \limits_ {n = 1} ^ \infty u_n$条件收敛。

例如，$\displaystyle\sum \limits_ {n = 1} ^ \infty \frac{(-1)^{n + 1}}{n}$，对于$u_{n + 1} + u_{n + 2} + \cdots +u_{n + p} $：

$$
u_{n + 1} + u_{n + 2} + \cdots +u_{n + p} = (-1)^{n + 2} (\frac{1}{n+1} - (\frac{1}{n+2} - \frac{1}{n+3}))
$$

由柯西收敛原理，$\displaystyle\sum \limits_ {n = 1} ^ \infty \frac{(-1)^{n + 1}}{n}$收敛。

**定理（Dirichlet判别法）：** 设$\displaystyle u_n \ge 0$, $\{ u_n\}$递减趋向于$0$，则$\displaystyle\sum \limits_ {n = 1} ^ \infty (-1)^{n + 1}u_n$收敛。

现在，我们考虑第一节遗留的问题：
$\displaystyle\sum \limits_ {n = 1} ^ \infty v_n u_n  = \sum \limits_ {k = n + 1} ^ {n + p} v_k u_k$

