## 定积分
*(Jensen Inequality)*: f(x)是下凸的函数，求证：
$$
f(\frac{x_1+x_2}{2})\le \frac{1}{x_2-x_1}\int_{x_1}^{x_2}f(t)  \mathrm{d}t\le \frac{f(x_1)+f(x_2)}{2}
$$

**证明：** 设$\displaystyle t=-s+2(\frac{x_1+x_2}{2})$,则$\mathrm{d}t=-\mathrm{d}x$
$$
\int_{x_1}^{x_2}f(t)  \mathrm{d}t=\int_{x_1}^{x_2}f(-s+2(x_1+x_2)/2)  \mathrm{d}s\le \int_{x_1}^{x_2}  \mathrm{d}s
$$

求极限：$\displaystyle \lim_{n \to \infty}\sum_{k=1}^{n-1}(1+\frac{k}{n})\sin \frac{k\pi}{n^2}$

$$
\begin{aligned}
u_k & = (1+\frac{k}{n})\sin\frac{k\pi}{n^2}  \\
& = (1+\frac{k}{n})(\frac{k\pi}{n^2}+o(\frac{1}{n^5}))  \\
& = k\frac{\pi}{n^2}+k^2\frac{\pi}{n^3}+o(\frac{1}{n^5})  \\
\end{aligned}
$$
$$
\sum_{k=1}^{n-1}u_k=\frac{n(n-1)\pi}{2n^2}+\frac{n(n-1)(2n-1)\pi}{6n^3}+o(\frac{1}{n^4})\to \frac{2}{3},n\to \infty
$$

(Trick: 变限积分)
 设 $f(x)$ 在$[0,1]$上连续可微且 $f(0)=f(1)=0$, 证明：对于所有的 $t\in [0,1]$, 都有 $\displaystyle f^2(t)\le \frac{1}{4}\int_{0}^{1}[f'(x)]^2  \mathrm{d}x$
**证明**
$$
\int_{0}^{t_0}[f'(x)]^2  \mathrm{d}x \int_{0}^{t_0} 1 \mathrm{d}x\ge (\int_{0}^{t_0}f'(x)  \mathrm{d}x)^2=f^2(t_0)
$$
$$
\int_{t_0}^{1}[f'(x)]^2  \mathrm{d}x\int_{t_0}^{1}1\mathrm{d}x\ge (\int_{t_0}^{1}f'(x))^2  \mathrm{d}x=f^2(t_0)
$$
$$
\int_{0}^{1}[f'(x)]^2  \mathrm{d}x\ge \frac{f^2(t_0)}{t_0}+ \frac{f^2(t_0)}{1-t_0}\ge 4f^(t_0)
$$