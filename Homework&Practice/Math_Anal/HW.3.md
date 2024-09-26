# 数学分析第三次作业

## 15.1.1

$$
\int_{0}^{+\infty}  \frac{\mathrm{d}x}{1+x^3}=\int_{0}^{+\infty}\frac{1}{(x^2-x+1)(x+1)}\mathrm{d}x=\int_{0}^{+\infty}(\frac{Ax+B}{x^2-x+1}+\frac{C}{x+1}) \mathrm{d}x
$$

解得：

$$
\begin{cases} A =-\frac{1}{3}  \\ B =\frac{2}{3} \\ C = \frac{1}{3} \end{cases}
$$

于是积分可以化为：

$$
\begin{aligned}
\int_{0}^{+\infty}\frac{-\frac{1}{3}x+\frac{2}{3}}{x^2-x+1}+\frac{\frac{1}{3}}{x+1}  \mathrm{d}x & = \int_{0}^{+\infty}\frac{-\frac{1}{6}\mathrm{d}(x-\frac{1}{2})^2}{(x-\frac{1}{2})^2+\frac{3}{4}}+\frac{\frac{1}{2}\mathrm{d}(x-\frac{1}{2})}{(x-\frac{1}{2})^2+\frac{3}{4}}+\frac{\frac{1}{3}\mathrm{d}(x+1)}{x+1}  \\
& = \left.\left\{ \frac{1}{6}\ln[(x-\frac{1}{2})^2+\frac{3}{4}]+\frac{1}{\sqrt{3}}\arctan\frac{2}{\sqrt{3}}(x-\frac{1}{2})+\frac{1}{3}\ln(x+1) \right\} \right|^{+\infty}_0    \\
\end{aligned}
$$

注意到：

$$
\left.\frac{1}{\sqrt{3}}\arctan\frac{2}{\sqrt{3}}(x-\frac{1}{2})\right|^{+\infty}_0=\frac{1}{\sqrt{3}}(\frac{\pi}{2}+\frac{\pi}{6})=\frac{2\sqrt{3}\pi}{9}
$$

以及

$$
\frac{1}{6}\ln[(x-\frac{1}{2})^2+\frac{3}{4}]+\frac{1}{3}\ln(x+1)=\frac{1}{6}\ln\left[ \frac{(x+1)^2}{(x-\frac{1}{2})^2+\frac{3}{4}} \right]
$$

当$x=0$和$x\to +\infty$时，上面的式子都是$\displaystyle \frac{1}{6}\ln 1=0$,所以原积分的值为$\frac{2\sqrt{3}\pi}{9}$

## 15.1.2

考虑$A_n=n\pi$以及区间$[A_{n-1},A_n]$，设$\displaystyle u_n=\int_{A_{n-1}}^{A_n}e^{-x}|\sin x|  \mathrm{d}x$。

$$
\int_{(2n-1)\pi}^{2n\pi}-e^{-x}\sin x \mathrm{d}x=\left.\frac{e^{-x}(\cos x+\sin x)}{2}\right|^{2n\pi}_{(2n-1)\pi}=\frac{e^{2n\pi}+e^{(2n-1)\pi}}{2}
$$

$$
\int_{2n\pi}^{(2n+1)\pi}e^x\sin x  \mathrm{d}x=\left. -\frac{e^{x}(\cos x+\sin x)}{2}\right|^{(2n+1)\pi}_{2n\pi}=\frac{e^{2n\pi}+e^{(2n+1)\pi}}{2}
$$

$$
\sum_{i=1}^{n}u_i=\frac{e^0+2(e^{-\pi}+e^{-2\pi\cdots+e^{-(n-1)\pi}})+e^{-n\pi}}{2}=\frac{1+e^{-n\pi}}{2}+\frac{e^{-\pi}(1-(e)^{-n+1})}{1-\frac{1}{e}}\to \frac{e^{-\pi +1}}{e-1},n\to \infty
$$

设$A\in [A_n,A_{n+1}]$,那么$\displaystyle \int_{A_n}^{A}e^{-x}|\sin x|  \mathrm{d}x=\left.(-1)^{n+1}\frac{e^{-x}(\sin x+\cos x)}{2}\right|^A_{A_n}\to 0 ,n\to \infty$

所以原积分值为$\displaystyle \frac{e^{-\pi +1}}{e-1}$

## 15.1.2.(1)

$$
\int_{0}^{A}\frac{1}{1+x|\sin x|}  \mathrm{d}x< \int_{0}^{A}\frac{1}{1+x}  \mathrm{d}x\to +\infty,A\to +\infty
$$

所以原积分发散。

## 15.1.2.(2)

考虑到$x^2e^{-x^2}$是偶函数，所以只需考虑$\displaystyle \int_{0}^{+\infty} x^2e^{-x^2} \mathrm{d}x$，又因为$e^{-x^2}$是$\displaystyle \frac{1}{x^4}$的低阶无穷小，所以$x^2e^{-x^2}$就是$\displaystyle \frac{1}{x^2}$的高阶无穷小。从而原级数是收敛的。

## 15.1.2.(3)

$$
\int_{-\infty}^{+\infty}\frac{x}{e^x+x^4}  \mathrm{d}x\le\int_{-1}^{+\infty}\left|\frac{x}{e^x+x^4}\right|  \mathrm{d}x+\int_{-\infty}^{-1}\left|\frac{x}{e^x+x^4} \right|\mathrm{d}x\le \int_{-1}^{+\infty}\left|\frac{x}{\frac{1}{e}+x^4}\right|  \mathrm{d}x+\int_{-\infty}^{-1}-\frac{1}{x^3}  \mathrm{d}x
$$

考虑：

$$
\int_{-1}^{+\infty}\left|\frac{x}{\frac{1}{e}+x^4}\right| =\int_{-1}^{0}-\frac{1}{2}\frac{\mathrm{d}(x^2)}{\frac{1}{e}+x^4} +\int_{0}^{+\infty} \frac{1}{2}\frac{\mathrm{d}x^2}{\frac{1}{e}+x^4} =\left.-\frac{1}{2}\sqrt{e}\arctan\sqrt{e}x\right|^{0}_{-1}+\left.\frac{1}{2}\sqrt{e}\arctan\sqrt{e}x\right|_{0}^{+\infty}
$$

上述的值为一个有界值，并且$\frac{1}{x^3}$是广义积分收敛的，所以原积分收敛。

## 15.1.2.(4)

注意到：

$$
\frac{\frac{\pi}{2}-\arctan x}{\frac{1}{x}}=\frac{-\frac{1}{1+x^2}}{-\frac{1}{x^2}}\to 1,x\to +\infty
$$

所以$\displaystyle \frac{\frac{\pi}{2}-\arctan x}{2}$和$\frac{1}{x}$是同阶的当$x\to +\infty$时，所以原被积函数就和$\frac{1}{x^2}$同阶，所以原积分收敛。

## 15.1.2.(5)

注意到：

$$
\ln(\cos \frac{1}{x}+\sin \frac{1}{x})\sim \ln (1+\frac{1}{x})\sim \frac{1}{x},x\to +\infty
$$

所以原积分发散。

## 15.1.3.(1)

由于$\ln x$对于$\forall q>0$, 是$x^q$的低阶无穷小,所以下列结论是显然的：

1. $p>1$时，原积分收敛
2. $p<1$时，原积分发散

考虑$p=1$时，由于$\displaystyle \frac{\ln x}{x}>\frac{1}{x},x>e$时，所以原积分发散

## 15.1.3.(2)

由于$p,q>0$，所以$\displaystyle \frac{x^p}{1+x^q}\sim \frac{x^p}{x^q}$

1. $q-p> 1$时，原积分收敛
2. $q-p\le 1$时, 原积分发散

## 15.(A).1

### 1.(1)

考虑$x\in (0,1)$时的情况。$\displaystyle f(x)=\frac{\sin\sqrt{x}}{\sqrt{x}(x+1)} \implies f(x)\to 1,x\to 0^+$, 并且$|f(x)|<1,x>0$

$$
\left| \frac{\sin\sqrt{x}}{\sqrt{x}(x+1)} \right|\le \frac{1}{\sqrt{x}(x+1)} \sim \frac{1}{x^{\frac{3}{2}}}
$$

所以说我们有：$\displaystyle \int_{1}^{+\infty}|f(x)|  \mathrm{d}x$收敛，又因为$f(x)$在$(0,1)$是有界并且可积的，所以$\displaystyle \int_{0}^{+\infty}f(x)  \mathrm{d}x$绝对收敛。

### 1.(2)

由于$\displaystyle \int_{2}^{A}\sin x  \mathrm{d}x$是有界的，又因为$\displaystyle \frac{1}{\ln x}$单调趋于零，所以由迪利克雷判别法可知原积分收敛。

再考虑$\displaystyle f(x)=\left| \frac{\sin x}{\ln x} \right| \ge \frac{\sin^2x}{\ln x}=\frac{1-\cos 2x}{2\ln x}=\frac{1}{2\ln x}-\frac{\cos 2x }{2\ln x}$。

其中$\displaystyle \int_{2}^{+\infty}\frac{1}{\ln x}  \mathrm{d}x$是发散的而$\displaystyle \int_{2}^{+\infty}\frac{\cos 2x}{2\ln x}  \mathrm{d}x$是收敛的。所以绝对值积分是发散的，所以原积分条件收敛。

### 1.(3)

$\displaystyle f(x)=\frac{\sin \frac{1}{x}}{x},x\in (1,+\infty)$是不变号的，所以原积分要么发散，要么绝对收敛，而$\displaystyle \sin \frac{1}{x}\sim \frac{1}{x},x\to +\infty\implies f(x)\sim \frac{1}{x^2},x\to +\infty$，所以原积分绝对收敛。

### 1.(4)

$\ln \ln x$对于$\forall p>0$, 都是$(\ln x)^p$的高阶无穷小，所以在$x$足够大时，$\displaystyle \frac{\ln \ln x}{\ln x}$是单调递减趋于零的，又因为$\displaystyle \int_{e}^{A}\sin x  \mathrm{d}x$是有界的，由*Direchlet* 判别法可知，原积分是收敛的。

再考虑$\displaystyle f(x)=\frac{\ln \ln x}{\ln x}\sin x$的绝对值 $|f(x)|$

$$
|f(x)|\ge \sin^2 x \frac{\ln \ln x}{\ln x} \ge \frac{1-\cos 2x}{2} \frac{1}{\ln x}, x>e^e
$$

不等号右侧的广义积分与 **1.(2)** 相同是发散的，所以原积分条件收敛。

### 1.(5)

首先$x\in (0,1)$时，$f(x)=x^{\mu}e^{-ax}\cos x$是有界连续的，所以$\displaystyle \int_{0}^{1} f(x) \mathrm{d}x$与$\displaystyle \int_{0}^{1}|f(x)|  \mathrm{d}x$是存在的

$x\in (1,+\infty)$时，$e^{-ax}$ 对于 $\forall p>0$, 都是 $x^p$ 的高阶无穷小, 所以$|f(x)|<\frac{1}{x^p}, p>1$，所以原积分绝对收敛
