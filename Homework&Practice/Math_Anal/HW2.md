# 数分第二次作业

## 14.4

### 1

#### (1)

**Solution**

$$
a_n =\begin{cases} \frac{1}{n!}&,n \text{为奇数} \\ -\frac{1}{n}&,n\text{为偶数} \end{cases}
$$

设$\displaystyle u_{n}=\frac{1}{(2n-1)!}\le \frac{1}{(2n-1)^2},n>3$, $\displaystyle v_{n}=-\frac{1}{2n}$, $\displaystyle S_n=\sum_{n=1}^{\infty}u_n$, 所以有：

$$
S_{2n}=1+\frac{1}{3!}+\sum_{k=3}^{n}u_k+\sum_{k=1}^n v_k<\sum_{k=3}^{n} \frac{1}{(2n-1)^2}-\sum_{k=1}^{n}\frac{1}{n}\to -\infty,n\to \infty
$$

同样的，我们可以得到：

$$
S_{2n-1}=1+\frac{1}{3!}+\sum_{k=3}^{n}u_k+\sum_{k=1}^n v_k<\sum_{k=3}^{n} \frac{1}{(2n-1)^2}-\sum_{k=1}^{n-1}\frac{1}{n}\to -\infty,n\to \infty
$$

所以原级数发散。

#### (2)

**Solution** 设$\displaystyle f(x)=\frac{\ln x}{\sqrt{x}}$, $\displaystyle f'(x)=\frac{2-\ln x}{2x\sqrt{x}}<0,\ x>e^2$, 所以当$n$足够大时侯$f(n)$是单调递减趋于零的。由莱布尼茨判别法即可得到：$\displaystyle \sum_{n=1}^{\infty}(-1)^{n+1}\frac{\ln n}{\sqrt{n}}$是收敛的。而$\displaystyle\frac{\ln n}{\sqrt{n}}>\frac{1}{\sqrt{n}}$，所以$\displaystyle \sum_{n=1}^{\infty} \frac{\ln n}{\sqrt{n}}$是发散的，故原级数条件收敛。

#### (3)

**Solution** 由于 $\displaystyle \sum_{n=1}^{\infty}(-1)^n\sin \frac{x}{n}$中,$n$足够大时候必然有 $\{\sin \frac{x}{n}\}$是单调递减的, 由莱布尼茨判别法$\displaystyle \sum_{n=1}^{\infty}(-1)^n \sin \frac{x}{n}$是收敛的。

而$\sin \frac{x}{n} \sim \frac{x}{n},n\to \infty$，不等式右边的求和级数是发散的，所以原级数条件收敛。

#### (4)

**Solution** 注意到:

$$
\begin{aligned}
\sin (\sqrt{n^2+1}\pi) & = \sin (\sqrt{n^2+1}\pi)-\sin(n\pi)  \\
& = 2\sin[\frac{\pi}{2}(\sqrt{n^2+1}-n)] \cos [\frac{\pi}{2} (\sqrt{n^2+1}+n)]  \\
\end{aligned}
$$

由于$n\to \infty$时，有以下结论：

1. $\displaystyle \sin[\frac{\pi}{2}(\sqrt{n^2+1}-n)]\sim \frac{\pi}{2}\frac{1}{\sqrt{n^2+1}+n}=\frac{\pi}{4n}$
2. $\displaystyle \cos [\frac{\pi}{2} (\sqrt{n^2+1}+n)]\sim \cos(n\pi)=(-1)^n$
   所以$\displaystyle \sum_{n=1}^{\infty}2\sin[\frac{\pi}{2}(\sqrt{n^2+1}-n)] \cos [\frac{\pi}{2} (\sqrt{n^2+1}+n)]\sim \sum_{n=1}^{\infty}(-1)^n\frac{\pi}{4n}$,由莱布尼茨判别法以及$\frac{1}{n}$级数性质：该级数条件收敛。

#### (5)

**Solution** $\displaystyle u_n=\exp (\ln(\frac{1\times 3\times 5\times \cdots}{2\times 4\times 6\times \cdots}))=\exp(\sum_{i=1}^{n}\ln (\frac{2i-1}{2i}))\sim \exp(\sum_{i=1}^{n}-\frac{1}{2i})\to 0$, $u_{n+1}/u_n=\frac{2n+1}{2n+2}<1$，所以$u_n$单减到零，所以原级数收敛

$\displaystyle u_n=\frac{(2n-1)!!}{(2n)!!}\implies R_n=n(\frac{u_n}{u_{n+1}}-1)=n(1+\frac{1}{2n+2}-1)\to \frac{1}{2}<1,n\to \infty, $ 所以原级数条件收敛。

#### (6)

**Solution** 注意到：$(-1)^{n(n+1)/2}$ 当$n$或$n+1$为4的倍数时 $(-1)^{n(n+1)/2}=1$，反之则为$-1$，所以 $(-1)^{n(n+1)/2}$ 有周期4，且在一个周期内和为0，所以 $\displaystyle \sum_{n=1}^{m}(-1)^{n(n+1)/2}$ 有界, 又因为 $\frac{1}{\sqrt{n}}$ 单调递减趋于零，所以原级数收敛，而$\displaystyle \sum_{n=0}^{\infty}\frac{1}{\sqrt{n}}$发散，所以原级数条件收敛。

#### (7)

**Solution** 由于$\sin \frac{n\pi}{12}$的周期性，有周期24且一个周期内和为零，$\displaystyle \sum_{n=1}^{m}\sin \frac{n\pi}{12}$ 是有界的, 又因为 $\displaystyle \frac{1}{\ln n}$ 单调递减趋于零，所以原级数收敛。

而我么考虑$|\sin \frac{n\pi}{12}|$,有一个子列 $\{ 1,1,1,1\cdots \}_{n}$，而且除了子列中的数其他数都大于等于零，所以$\displaystyle  S_k=|\sum_{n=2}^{k}\frac{\sin \frac{n\pi}{12}}{\ln n}|> \sum_{n=1}^{[\frac{k}{6}]-1}\frac{1}{\ln 6n}$发散，所以原级数条件收敛

#### (8)

$$
\begin{aligned}
\sum_{n=1}^{m}(-1)^{n-1}\sin n & = \frac{1}{\cos \frac{1}{2}}\sum_{n=1}^{m}(-1)^n\sin n\cos \frac{1}{2}  \\
& = \frac{1}{\cos \frac{1}{2}}\sum_{n=1}^{m}(-1)^{n-1}[\sin (n-\frac{1}{2})+\sin(n+\frac{1}{2})]  \\
& = \frac{1}{\cos \frac{1}{2}}[ \sin \frac{1}{2}+(-1)^{m-1}\sin(m+\frac{1}{2})] \\
\end{aligned}
$$

所以$\displaystyle \sum_{n=1}^{m} (-1)^{n-1}\sin n$是有界的，又因为$\frac{1}{n}$单减到零，所以原级数收敛。

$$
\frac{|\sin n|}{n}\ge \frac{|sin^2 n|}{n}=\frac{1-\cos^2 \frac{n}{2}}{2n}
$$

不等式右边的求和级数是发散的，所以原级数条件收敛。

### 2

由于$\{ a_k \}$条件收敛：
设 $\displaystyle \sum_{k=1}^{\infty} a_k=A$，所以$\forall \epsilon>0,\exists N>0,n>N$时，$\displaystyle |\sum_{k=1}^{n}a_k-A|<\epsilon$

$$
|\sum_{k=1}^{n} a_k-A|<\epsilon \implies A-\epsilon<\sum_{k=1}^{n}a_k^+ -\sum_{k=1}^{n}a_k^- <A+\epsilon
$$

设$\displaystyle U_n=\sum_{k=1}^{n}a_k^+, V_n=\sum_{k=1}^{n}a_k^-$，则$U_n,V_n\to \infty ,n\to \infty$, $\displaystyle \frac{U_n-V_n}{V_n}\to 0 ,n\to \infty$, 即 $\displaystyle \lim_{n \to \infty}\frac{U_n}{V_n}=1$

### 3

#### (1)

$$
\prod_{n=1}^{m} \frac{(n+1)^2}{n(n+2)}=\frac{2(m+1)}{m+2} \to 2,m\to \infty
$$

所以原级数收敛。

#### (2)

$$
\ln\prod_{n=1}^{m}\sqrt[n]{1+\frac{1}{n}}=\sum_{n=1}^{m}\frac{1}{n}\ln(1+\frac{1}{n})\sim \sum_{n=1}^{m}\frac{1}{n^2}
$$

与之同阶的级数是收敛的，所以原级数收敛。

#### (3)

$$
\ln \prod_{n=1}^{m} \frac{n}{\sqrt{n^2+1}}=-\frac{1}{2}\sum_{n=1}^{m}\ln (1+\frac{1}{n^2})=-\frac{1}{2}\sum_{n=1}^{m}\frac{1}{n^2}
$$

与之同阶的级数是收敛的，所以原级数收敛。

#### (4)

$$
\ln\prod_{n=1}^{\infty}\sqrt[n]{\ln(n+x)-\ln n}=\sum_{n=1}^{\infty}\frac{1}{n}[\ln(\ln(1+\frac{x}{n}))] \sim \sum_{n=1}^{\infty}\frac{\ln \frac{x}{n}}{n}=\sum_{n=1}^{\infty} \frac{\ln x-\ln n}{n},n\to \infty
$$

而$\frac{\ln x-\ln n}{n}<-\frac{1}{n}, n>ex$时，不等号右边的求和级数是发散的，所以原级数发散。
