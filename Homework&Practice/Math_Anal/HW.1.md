## 数学分析 HW.1

### 14.1

1.(1) 设 $\displaystyle u_n=\frac{n}{(n+1)(n+2)(n+3)}$

$$
\begin{aligned}
u_n & = (1-\frac{1}{n+1})\frac{1}{(n+2)(n+3)}  \\
& = (\frac{1}{n+2}-\frac{1}{n+3})-\frac{1}{(n+1)(n+2)(n+3)}  \\
& = (\frac{1}{n+2}-\frac{1}{n+3})-\frac{1}{2}[\frac{1}{(n+1)(n+2)}-\frac{1}{(n+2)(n+3)}]  \\
\end{aligned}
$$

$$
\displaystyle \sum_{n=1}^{\infty}u_n=\frac{1}{3}-\frac{1}{12}=\frac{1}{4}
$$

1.(2) 设 $\displaystyle u_n=\frac{2n-1}{2^n}$,我们有$\displaystyle u_n=\frac{2n+1}{2^{n-1}}-\frac{2n+3}{2^n}$,而$\displaystyle \frac{2n+3}{2^n}\to 0$，当$n\to \infty$时，那么$\displaystyle \sum_{n=1}^{\infty}u_n=3$

1.(3) 设 $\displaystyle u_n=\sqrt{n+2}-2\sqrt{n+1}+\sqrt{n}$，则$\displaystyle u_n=\frac{1}{\sqrt{n+2}+\sqrt{n+1}}-\frac{1}{\sqrt{n+1}+\sqrt{n}}$，而$\displaystyle \frac{1}{\sqrt{n+2}+\sqrt{n+1}}\to 0,\ n\to \infty$

$$
\sum_{n=1}^{\infty}u_n=0-\frac{1}{\sqrt{2}+1}=1-\sqrt{2}
$$

### 14.2

(1)

$$
\sum_{n=1}^{\infty}\frac{\prod_{i=1}^n(3i-1)}{\prod_{i=1}^{n}(4i-3) }
$$

**Solution**

$\displaystyle u_n=\cfrac{\prod_{i=1}^n(3i-1)}{\prod_{i=1}^{n}(4i-3) } $,$\displaystyle\frac{u_{n+1}}{u_n}=\frac{3n+2}{4n+1}<\frac{8}{9},\ n>2$.

所以原级数收敛。
(2)

$$
\sum_{n=1}^{\infty}\frac{3^n}{n!}
$$

**Solution**

$$
u_n=\frac{3^n}{n!}\implies \frac{u_{n+1}}{u_n}=\frac{3n}{n+1}\to 3>1,\ n\to \infty
$$

所以原级数发散

(3)

$$
\sum_{n=1}^{\infty}\frac{3^nn!}{(2n)!}
$$

**Solution**

$$
u_n=\frac{3^nn!}{(2n)!}\implies \frac{u_{n+1}}{u_n}=\frac{3(n+1)}{(2n+1)(2n+2)}\to 0,\ n\to \infty.
$$

原级数收敛。

(4)

$$
\sum_{n=1}^{\infty}\frac{(n!)^2}{(2n)!}
$$

**Solution**

$$
u_n=\frac{(n!)^2}{(2n)!}\implies \frac{u_{n+1}}{u_n}=\frac{(n+1)^2}{(2n+1)(2n+2)}\to \frac{1}{4},\ n\to \infty
$$

原级数收敛。
(5)

$$
\sum_{n=2}^{\infty}\frac{1}{(\ln n)^n}
$$

**Solution**

$[(\ln n)^n]^{\frac{1}{n}}=\ln n>1,n>3$

所以原级数发散。
(6)

$$
\sum_{n=1}^{\infty}\left( \frac{n+1}{2n+1} \right)^n
$$

**Solution**

$$
u_n=\left( \frac{n+1}{2n+1} \right)^n\implies \sqrt[n]{u_n}=\frac{n+1}{2n+1}\to \frac{1}{2}<1,\ n\to \infty
$$

原级数收敛。

(7)

$$
\sum_{n=1}^{\infty}\frac{3n^3+1}{2^n}
$$

**Solution**

$\displaystyle (\frac{3n^3+1}{2^n})^{\frac{1}{n}}=\frac{(3n^3+1)^{\frac{1}{n}}}{2} \rightarrow\frac{1}{2}$

原级数收敛。

(9)

$$
\sum_{n=1}^{\infty}\sin^2\frac{1}{n}
$$

**Solution**

$\displaystyle\sin^2\frac{1}{n} \sim\frac{1}{n^2},n\rightarrow0 $

原级数收敛。

(11)

$$
\sum_{n=1}^{\infty}\frac{1}{(n^2-1)^{\frac{1}{3}}}
$$

**Solution**

$\displaystyle\frac{1}{(n^2-1)^{\frac{1}{3}}} \sim\frac{1}{n^{\frac{2}{3}}}  ,n \to \infty $

原级数发散。

(15)

$$
\sum_{n=2}^{\infty}\frac{1}{(\ln n)^k}
$$

**Solution**

$\displaystyle\frac{1}{\ln n}>\frac{1}{n^{\frac{1}{k}}}, 当n足够大的时候$.$\displaystyle \frac{1}{(\ln n)^k}>\frac{1}{n}$

原级数发散。

(17)

$$
\sum(1-\cos\frac{x}{n})\ (x\in\mathbb{R})
$$

**Solution**

$\displaystyle1-\cos\frac{x}{n}\sim\frac{(\frac{x}{n})^2}{2}$

原级数收敛。

(19)

$$
\sum(\frac{1}{\sqrt{n}}-\sqrt{\ln(1+\frac{1}{n})})
$$

**Solution**

$\displaystyle\frac{1}{\sqrt{n}}-\sqrt{\ln(1+\frac{1}{n})}=\frac{\frac{1}{n}-\ln(1+\frac{1}{n})}{\frac{1}{\sqrt{n}}+\sqrt{\ln(1+\frac{1}{n})}}$,考虑 *Taylor Formula*:

$$
\frac{1}{n}-\ln(1+\frac{1}{n})=\frac{1}{n}-(\frac{1}{n}-\frac{1}{2n^2}+o(\frac{1}{n^2}))=\frac{1}{2n^2}+o(\frac{1}{n^2})
$$

$$
\sqrt{\frac{1}{n}}+\sqrt{\ln(1+\frac{1}{n})}>2\sqrt{\ln (1+\frac{1}{n})}
$$

所以：

$$
\frac{\frac{1}{n}-\ln(1+\frac{1}{n})}{\frac{1}{\sqrt{n}}+\sqrt{\ln(1+\frac{1}{n})}}<\frac{\frac{1}{2n^2}}{2\sqrt{\ln(1+\frac{1}{n})}}\sim\frac{1}{n^{\frac{5}{2}}}
$$

原级数收敛。

(21)

$$
\sum_{n=2}^{\infty}\frac{1}{\ln(n!)}
$$

**Solution**

$\ln(n!)=\displaystyle\sum_{i=1}^{n}\ln i$。根据积分不等式可以得到以下估计：

$$
\int_{1}^{n} \ln x \mathrm{d}x<\sum_{i=1}^{n}\ln i<\int_{1}^{n+1}\ln x  \mathrm{d}x \tag{2.1}
$$

或者直接使用放缩：

$$
\ln(n!)<n\ln n
$$

$$
\frac{1}{\ln(n!)}>\frac{1}{n\ln n}
$$

$$
\sum\frac{1}{n(\ln n)^p}\Rightarrow\begin{cases} \mathrm{covergent}, p>1&  \\ \mathrm{divergent}, 0<p\le1&  \end{cases}\tag{2.2}
$$

原级数发散。

### 14.3

1 设$\displaystyle u_n=\left|\frac{\alpha(\alpha-1)(\alpha-2)\cdots(\alpha-n+1)}{n!}\right|$.

$$
\frac{u_n}{u_{n+1}}=\left|\frac{n+1}{\alpha-n}\right|
$$

当 $n$ 足够大的时候，$\alpha-n<0$

$$
\frac{u_n}{u_{n+1}}=\frac{n+1}{n-\alpha}
$$

$$
R_n=n(\frac{u_n}{u_{n+1}}-1)=\frac{n}{n-\alpha}(\alpha +1)\to \alpha+1>1, \ n\to \infty
$$

由*Raabe*判别法，原级数收敛。

2 (1) $\displaystyle u_n=\frac{\sqrt{n!}}{(a+1)(a+\sqrt{2})\cdots(a+\sqrt{n})}$

$$
\frac{u_n}{u_{n+1}}=\frac{a+\sqrt{n+1}}{\sqrt{n+1}}
$$

$$
R_n=n(\frac{u_n}{u_{n+1}}-1)=n \frac{a}{\sqrt{n+1}}\to \infty,\ n\to \infty
$$

所以原级数收敛。

2 (2) $\displaystyle u_n=\frac{n!n^{-p}}{q(q+1)\cdots(q+n)}$

$$
\begin{aligned}
\frac{u_n}{u_{n+1}} &=\frac{q+n+1}{n+1} \left(1+\frac{1}{n}\right)^p\\
&=(1+\frac{q}{n+1})\left( 1+\frac{1}{n} \right)^p \\
&=\left( 1+\frac{q}{n+1} \right)\left( 1+\frac{p}{n}+\frac{p(p-1)}{2n^2}+o(\frac{1}{n^2}) \right) \\
&=1+\frac{q}{n+1}+\frac{p}{n}+\frac{pq}{n(n+1)}+\frac{p(p-1)}{2n^2}+o(\frac{1}{n^2})\\
&=1+\frac{p}{n}+\frac{q}{n}-\frac{q}{n(n+1)}+o(\frac{1}{n\ln n})\\
&=1+\frac{p+q}{n}+o(\frac{1}{n\ln n})
\end{aligned}
$$

由 *Raabe* 判别法：

$\displaystyle n(\frac{u_n}{u_{n+1}}-1)\to p+q,\ n\to \infty$

1. 当$p+q<1$时，原级数发散
2. 当$p+q>1$时，原级数收敛
3. 当$p+q=1$时，由高斯判别法：$\displaystyle \frac{u_n}{u_{n+1}}=\lambda+\frac{\mu}{n}+\frac{\nu}{n\ln n}+o(\frac{1}{n\ln n})$ 中的$\lambda=\mu=1,\nu<1$可知级数发散。
