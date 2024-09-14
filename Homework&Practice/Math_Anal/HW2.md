# 数分第二次作业

## 14.4

### 1

#### (1)

**Solution**

$$
a_n =\begin{cases} \frac{1}{n!}&,n \text{为奇数} \\ -\frac{1}{n}&,n\text{为偶数} \end{cases}
$$

设$\displaystyle u_{n}=\frac{1}{(2n-1)!}\le \frac{1}{(2n-1)^2}\frac{1}{(2n-1)^2},n>3$, $\displaystyle v_{n}=-\frac{1}{2n}$, $\displaystyle S_n=\sum_{n=1}^{\infty}u_n$, 所以有：

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

**Solution** 设$\displaystyle u_n=\frac{(2n-1)!!}{(2n)!!}$, $\displaystyle \frac{u_{n+1}}{u_n}=\exp (\ln )$
