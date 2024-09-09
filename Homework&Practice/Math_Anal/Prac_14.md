**练习14.2**
*（奇数题号）2024/9/3*
(1)

$$
\sum_{n=1}^{\infty}\frac{\prod_{i=1}^n(3i-1)}{\prod_{i=1}^{n}(4i-3) }
$$

**Solution**

$\displaystyle u_n=\cfrac{\prod_{i=1}^n(3i-1)}{\prod_{i=1}^{n}(4i-3) } $,$\displaystyle \frac{u_{n+1}}{u_n}=\frac{3n+2}{4n+1}<\frac{8}{9},when\ n>2$.
所以原级数收敛。
(5)

$$
\sum_{n=2}^{\infty}\frac{1}{(\ln n)^n}
$$

**Solution**

$[(\ln n)^n]^{\frac{1}{n}}=\ln n>1,n>3$
所以原级数发散。
(7)

$$
\sum_{n=1}^{\infty}\frac{3n^3+1}{2^n}
$$

**Solution**

$\displaystyle (\frac{3n^3+1}{2^n})^{\frac{1}{n}}=\frac{(3n^3+1)^{\frac{1}{n}}}{2} \rightarrow \frac{1}{2}$
原级数收敛。

(9)

$$
\sum_{n=1}^{\infty}\sin^2\frac{1}{n}
$$

**Solution**

$\displaystyle \sin^2 \frac{1}{n} \sim \frac{1}{n^2},n\rightarrow 0 $
原级数收敛。

(11)

$$
\sum_{n=1}^{\infty}\frac{1}{(n^2-1)^{\frac{1}{3}}}
$$

**Solution**

$\displaystyle \frac{1}{(n^2-1)^{\frac{1}{3}}} \sim \frac{1}{n^{\frac{2}{3}}}  $
原级数发散。

(15)

$$
\sum_{n=2}^{\infty}\frac{1}{(\ln n)^k}
$$

**Solution**

$\displaystyle \frac{1}{\ln n}>\frac{1}{n^{\frac{1}{k}}}, $when n is large enough.$\displaystyle \frac{1}{(\ln n)^k}>\frac{1}{n}$
原级数发散。

(17)

$$
\sum(1-\cos \frac{x}{n})\ (x\in \mathbb{R})
$$

**Solution**

$\displaystyle 1-\cos \frac{x}{n}\sim \frac{(\frac{x}{n})^2}{2}$
原级数收敛。

(19)

$$
\sum(\frac{1}{\sqrt{n}}-\sqrt{\ln(1+\frac{1}{n})})
$$

**Solution**

$\displaystyle \frac{1}{\sqrt{n}}-\sqrt{\ln(1+\frac{1}{n})}=\frac{\frac{1}{n}-\ln(1+\frac{1}{n})}{\frac{1}{\sqrt{n}}+\sqrt{\ln(1+\frac{1}{n})}}$,consider *Taylor Formula*:

$$
\frac{1}{n}-\ln(1+\frac{1}{n})=\frac{1}{n}-(\frac{1}{n}-\frac{1}{2n^2}+o(\frac{1}{n^2}))=\frac{1}{2n^2}+o(\frac{1}{n^2})
$$

$$
\sqrt{\frac{1}{n}}+\sqrt{\ln(1+\frac{1}{n})}>2\sqrt{\ln (1+\frac{1}{n})}
$$

Then

$$
\frac{\frac{1}{n}-\ln(1+\frac{1}{n})}{\frac{1}{\sqrt{n}}+\sqrt{\ln(1+\frac{1}{n})}}<\frac{\frac{1}{2n^2}}{2\sqrt{\ln(1+\frac{1}{n})}}\sim \frac{1}{n^{\frac{5}{2}}}
$$

原级数收敛。

(21)

$$
\sum_{n=2}^{\infty}\frac{1}{\ln(n!)}
$$

**Solution**

$\ln(n!)=\displaystyle \sum_{i=1}^{n}\ln i$.According ==integral inequlity==, the estimate of this value is:

$$
\int_{1}^{n} \ln x \mathrm{d}x<\sum_{i=1}^{n}\ln i<\int_{1}^{n+1}\ln x  \mathrm{d}x \tag{2.1}
$$

or use scaling method:

$$
\ln(n!)<n\ln n
$$

$$
\frac{1}{\ln(n!)}>\frac{1}{n\ln n}
$$

$$
\sum\frac{1}{n(\ln n)^p}\Rightarrow \begin{cases} \mathrm{covergent}, p>1&  \\ \mathrm{divergent}, 0<p\le 1&  \end{cases}\tag{2.2}
$$

原级数发散

大概前几题用到达朗贝尔和柯西判别法，后面的几题都是估计，牢记几个不等式和*Taylor Formula*。

---

**（14 A）**
*2024/9/4*

1.$\{a_n\}$递减并且级数$\displaystyle \sum_{n=1}^{\infty}a_n$收敛，求证：$\lim\limits_{n \to \infty}na_n=0$
**Proof** $\ \ \forall \varepsilon>0,\exists N,when\ n>N,\forall p,\displaystyle \sum_{k= n+1}^{n+p}a_k<\varepsilon,$when $p=n$,the form is

$$
\displaystyle \sum_{k= n+1}^{2n}a_k<\varepsilon
$$

我们这样思考，$na_{2n}$是n个$a_{2n}$相加，consider

$$
na_{2n}<\sum_{k= n+1}^{2n}a_k<\varepsilon
$$

namely,

$$
\lim_{n \to \infty} 2na_{2n}=0
$$

Similarly,consider odd terms:

$$
\lim_{n \to \infty}(2n+1)a_{2n+1}=0
$$

1. (4) 判断收敛发散

$$
\sum_{n=3}^{\infty}\frac{1}{n(\ln n)^p(\ln \ln n)^q}
$$

**Solution**

First there is a fact:

$$
1<\ln \ln n<(\ln n)^s,\forall \ 0<s<1,n\rightarrow \infty
$$

这样便可以得出$p>1$或$0<p<1$时的敛散性。

3. (组合)

$\{a_n\}$递减，且非负，求证：$\displaystyle \sum_{n=1}^{\infty}a_n$和$\displaystyle \sum_{k= 1}^{\infty}2^ka_{2^k}$同敛散性

4. (柯西收敛定理)

设$\{a_n\}$递增正数数列,求证：$\displaystyle \sum_{n=1}^{\infty}(1-\frac{a_n}{a_{n+1}})$在$\{a_n\}$有界时收敛，无界时发散。

**Proof**

(1) when $\{a_n\}$ is bounded,

$$
(1-\frac{a_n}{a_{n+1}})=\frac{a_{n+1}-a_n}{a_{n+1}}
$$

note the sum as $S_n$

$$
S_n=\frac{a_2-a_1}{a_2}+\frac{a_3-a_2}{a_3}+ \cdots +\frac{a_{n+1}-a_n}{a_{n+1}}\le \frac{a_{n+1}-a_1}{a_2}
$$

i.e. reduce all demominators to $a_2$ ,and then sum numerators. $\le $ 右边的数是有界量，原级数收敛。

(2) when $a_{n}$ is unbounded:
用柯西收敛原理证明原级数不收敛。首先，我们由$\{a_n\}$发散可以得到一个结论：

$$
\forall n\in \mathbf{N},M\in \mathbf{R^+},\exists p>0,\mathbb{s.t.}\ \ a_{n+p}=Ma_n
$$

where $p$ is depend on $M,n$
每次以上次的$a_{n+p}$赋值为$M$，我们就可以得到一个数列 $\{ p_m\}$以及$\displaystyle \{\frac{a_{n+p_{m}}-a_n}{a_{n+p_m}}\}\rightarrow 1^- >0  $
对于一个给定的$n$

$$
\sum_{k= n+1}^{n+p}(1-\frac{a_n}{a_{n+1}})>\frac{a_{n+p}-a_n}{a_{n+p}}
$$

依次在$\{p_m\}$取p，又因为上述的数列收敛到1,即：$\exists\varepsilon_0>0\forall n>0,\exists ,p>0$，$\displaystyle \sum_{k= n+1}^{n+p}(1-\frac{a_n}{a_{n+p}})>\frac{a_{n+p}-a_n}{a_{n+p}}$ (可以取到在1附近的值) $ \ge \varepsilon_0$

所以原级数发散

5. (ln n的阶估计)

$\displaystyle \sum_{n=2}^{\infty}\frac{1}{(\ln n)^{\ln n}},\sum_{n=3}^{\infty}\frac{1}{(\ln n)^{\ln\ln n}},\sum_{n=2}^{\infty}\frac{1}{(\ln\ln n)^{\ln n}}$

**Solution**

(1). 

$$
\ln n>3,n>e^3\Rightarrow \frac{1}{(\ln n)^{\ln n}} <\frac{1}{3^{\ln n}}=\frac{1}{n^{\ln 3}}\ (\sum^{\infty}\frac{1}{n^{\ln 3}}\mathrm{ \ is\  convegent})
$$


(2). $(\ln n)^{\ln \ln n}=e^{(\ln \ln n)^2}<e^{[(\ln n)^{\frac{1}{2}}]^2}=n$,所以$\displaystyle \sum_{n=3}^{\infty}\frac{1}{(\ln n)^{\ln \ln n}}>\sum_{n=3}^{\infty}\frac{1}{n}$
6.
7. (裂项相消) (integral inequality)

$\displaystyle u_n>0,S_n=\sum_{n=1}^{\infty}$ is divergent.Argue that $\displaystyle \sum_{n=1}^{\infty}\frac{u_n}{S_n}$ is convegent,$\displaystyle \sum_{n=1}^{\infty}\frac{u_n}{S_n^{2}}$ is divergent, and $\displaystyle \sum_{n=1}^{\infty}\frac{u_n}{S^{1+\sigma}}$ is convegent.

**Solution**

(1). $ \displaystyle u_n=S_n-S_{n-1} \implies \sum_{n=1}^{\infty}\frac{u_{n}}{S_{n}}=\sum_{n=1}^{\infty}(\frac{S_{n}-S_{n-1}}{S_n}) $. According 4. , $\displaystyle \sum_{n=1}^{\infty}\frac{u_n}{S_n}$ is divergent.

(2). $\displaystyle \sum_{n=1}^{\infty}\frac{u_n}{S_n^{2}}<\sum_{n=1}^{\infty}\frac{S_n-S_{n-1}}{S_nS_{n-1}}=\sum_{n=1}^{\infty}(\frac{1}{S_{n-1}}-\frac{1}{S_{n}})=\sum_{n=1}^{\infty}(\frac{1}{S_1}-\frac{1}{S_n})=\frac{1}{S_1}$

(3). consider

$$
\displaystyle \frac{u_n}{S^{1+\sigma}}=\frac{S_n-S_{n-1}}{S^{1+\sigma}}<\int_{S_{n-1}}^{S_n}\frac{1}{x^{1+\sigma}}  \mathrm{d}x \tag{A.1}
$$

,

$$
\displaystyle \sum_{n=1}^{\infty}\frac{u_n}{S^{1+\sigma}}<\lim_{n \to \infty}\int_{S_1}^{S_n}\frac{1}{x^{1+\sigma}}  \mathrm{d}x=\lim_{n \to \infty}\left. -\frac{1}{\sigma}\frac{1}{x^{\sigma}} \right|_{S_1}^{S_n}=\frac{1}{\sigma S_1^{\sigma}}
$$
