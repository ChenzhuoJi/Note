# Practice.15(A)

## 2

设函数$f(x)$在$[a,+\infty)$上一直连续并且广义积分$\displaystyle \int_{a}^{\infty}f(x)  \mathrm{d}x$收敛，求证：$\displaystyle \lim_{x \to \infty}f(x)=0$

**证明：** 反证法：假设$\displaystyle \exists \{x_n\}\to \infty,\forall N,\exists \epsilon_0, n_0>N,f(x_{n_0})\ge \epsilon_0$,$\forall \epsilon >0,\exists \delta>0$,

当：$\displaystyle |x_1-x_2|<\delta,|f(x_1)-f(x_2)|<\epsilon$,

设$\displaystyle x\in [x_{n_k}-\delta,x_{n_k}+\delta]$, $|\displaystyle f(x)-f(x_{n_k})|<\frac{\epsilon_0}{2}$, $\displaystyle f(x)\ge f(x_{n_k})-\frac{\epsilon_0}{2}=\frac{\epsilon_0}{2}$, 那么：

$$
\int_{x_n-\delta}^{x_n+\delta}  f(x)\mathrm{d}x\ge \frac{\epsilon_0}{2} \times  2\delta=\epsilon_0\delta
$$

这说明$\displaystyle \int_{a}^{\infty} f(x) \mathrm{d}x$发散。

## 3

设函数$f(x)$连续可导，广义积分$\displaystyle \int_{a}^{\infty} f(x) \mathrm{d}x$和$\displaystyle \int_{a}^{\infty} f'(x) \mathrm{d}x$收敛，求证$ \displaystyle \lim_{x \to \infty}f(x)=0$

**证明：** $\displaystyle \lim_{A \to \infty}\int_{a}^{A}f'(x)  \mathrm{d}x=\lim_{A \to \infty}[f(A)-f(a)]$, 即：$\displaystyle \lim_{A \to \infty}f(A)=f(a)+\int_{a}^{\infty} f(x) \mathrm{d}x$，极限是是存在的。

1. $f(x)$在$[a,2M]$上连续 $\implies$ $f(x)$在$[a,2M]$上一致连续。
2. $\displaystyle \forall \epsilon>0,\exists M>0$, 当$A'>A>M$时，$|f(A')-f(A)|<\epsilon$, 所以$f(x)$在$[M,+\infty)$上一致连续。
   综上可得：$f(x)$在$[a,+\infty)$上一致连续。

由第2题结论便可以得证。

## 4

设$f(x)$在$[a,+\infty)$上单调并且广义积分$\displaystyle \int_{a}^{\infty}f(x)  \mathrm{d}x$收敛，求证$\displaystyle \lim_{x \to \infty}xf(x)=0$

**证明：** 由题意可得：$\forall \epsilon>0,\exists M,A'>A>M>0$时, $|\displaystyle \int_{A}^{A'}f(x)  \mathrm{d}x|<\epsilon$,若考虑$f(x)$单增：

$$
(A'-A)f(A)<\int_{A'}^{A}f(x)  \mathrm{d}x<(A'-A)f(A')
$$

1. $|f(A)|>|f(A')|\implies f(A)<0$时，取$A'=2A\implies 0<Af(A)-A'f(A)=-Af(A)<\epsilon$
2. $|f(A)|<|f(A')|\implies f(A')>0$时，取$A=\frac{1}{2}A'\implies 0<Af(A)-A'f(A)=\frac{1}{2}A'f(A')<\epsilon$

综上可得$\displaystyle \lim_{x \to \infty}xf(x)=0$

## 6

设函数$f(x)$在$[0,+\infty)$上连续并且$\displaystyle \lim_{x \to \infty}f(x)=A$, 求证：

$$
\lim_{\alpha \to 0^+}\alpha \int_{0}^{+\infty} e^{-\alpha x}f(x) \mathrm{d}x=A
$$

**证明：** 首先我们注意到：

$$
\int_{0}^{\infty}e^{-x}  \mathrm{d}x=1
$$

$$
\alpha \int_{0}^{+\infty} e^{-\alpha x}f(x) \mathrm{d}x=\int_{0}^{+\infty}e^{-x}f(\frac{x}{\alpha})  \mathrm{d}x
$$

所以：$\displaystyle \int_{0}^{\infty}e^{-x}f(\frac{x}{\alpha})  \mathrm{d}x-A=\int_{0}^{\infty}e^{-x}(f(\frac{x}{\alpha})-A)  \mathrm{d}x$, 设 $\displaystyle g(\frac{x}{\alpha})=f(\frac{x}{\alpha})-A$。

$\forall \epsilon>0$

考虑$\delta>0$, $\displaystyle \int_{\delta}^{\infty}e^{-x}g(\frac{x}{\alpha})  \mathrm{d}x+\int_{0}^{\delta}e^{-x}g(\frac{x}{\alpha})  \mathrm{d}x$。

其中$\displaystyle  \lim_{x \to \infty}g(x)=0$, 所以$\displaystyle \exists M,|g(x)|<M\implies \int_{0}^{\delta}e^{-x}g(\frac{x}{\alpha})  \mathrm{d}x<\int_{0}^{\delta}e^{-x}M  \mathrm{d}x=$, 取$\displaystyle \delta=-\ln(1-\frac{\epsilon}{2M})\implies\int_{0}^{\delta}e^{-x}g(\frac{x}{\alpha})  \mathrm{d}x\le \frac{\epsilon}{2}$

然后考虑$\displaystyle \int_{\delta}^{+\infty}e^{-x}g(\frac{x}{\alpha})  \mathrm{d}x$, 由于$\displaystyle \exists X_0, x\ge X_0$时，$\displaystyle g(x)<\frac{\epsilon}{2e^{-\delta}}$,取$\displaystyle \alpha=\frac{\delta}{X_0}\implies\int_{\delta}^{+\infty} e^{-x}g(\frac{x}{\alpha}) \mathrm{d}x\le e^{-\delta}\times \frac{\epsilon}{2e^{-\delta}}=\frac{\epsilon}{2}$

上述讨论的两个部分和在取适当的$\delta,\alpha$相加后小于$\epsilon$, 所以原式收敛于0.

## 7

设广义积分$\displaystyle \int_{a}^{+\infty}f(x)  \mathrm{d}x$收敛且$g(x)$有界，问广义积分$\displaystyle \int_{a}^{+\infty}f(x)g(x)  \mathrm{d}x$是否必然收敛?

未必，我们考虑$\displaystyle f(x)=g(x)=\frac{\sin x}{\sqrt{x}}$

$$
\boxed{\int_{1}^{+\infty}\frac{\sin x}{x^p}  \mathrm{d}x\ \begin{cases} \text{绝对收敛}, & p>1 \\ \text{条件收敛}, &0<p\le 1 \\ \text{发散} , & p\le 0 \end{cases}}
$$

$\displaystyle \int_{a}^{+\infty}\frac{\sin x}{\sqrt{x}}  \mathrm{d}x$收敛，但是 $\displaystyle \int_{a}^{+\infty}\frac{\sin ^2x}{x}  \mathrm{d}x=\int_{a}^{+\infty}\frac{1}{2x}-\frac{\cos 2x}{2x}  \mathrm{d}x$ 时发散的。

## 20

设$f(x)$在区间$[0,+\infty)$上可导，满足$f(0)>0,f'(0)\ge 0$,并且$\displaystyle \int_{0}^{+\infty}  \frac{\mathrm{d}x}{f(x)+f'(x)}$收敛，求证：$\displaystyle \int_{0}^{+\infty}  \frac{\mathrm{d}x}{f(x)}$收敛。

**证明：** 首先：$f(x)>0,f'(x)\ge 0\implies f(x)+f'(x)>0$。注意到：

$$
\displaystyle -\int_{0}^{A}  \frac{\mathrm{d}x}{f(x)+f'(x)}+\int_{0}^{A}\frac{\mathrm{d}x}{f(x)}=\int_{0}^{A} \frac{f'(x)}{[f(x)+f'(x)]f(x)}  \mathrm{d}x\le \int_{0}^{A}    \left[ \frac{f'(x)}{f^2(x)} \right] \mathrm{d}x=\frac{1}{f(A)}-\frac{1}{f(0)}
$$

即:

$$
0\le \int_{0}^{+\infty}\frac{1}{f(x)}  \mathrm{d}x\le \frac{1}{f(A)}-\frac{1}{f(0)}=\int_{0}^{+\infty}\frac{1}{f(x)+f'(x)}  \mathrm{d}x\le \int_{0}^{+\infty}\frac{1}{f(x)+f'(x)}  \mathrm{d}x
$$

## 月考
$\displaystyle \int_{0}^{+\infty}\sin x^2  \mathrm{d}x$的敛散性。

$\displaystyle t=x^2,\mathrm{d}x=\frac{\mathrm{d}t}{2x}=\frac{\mathrm{d}t}{2\sqrt{t}}$
$$
\int_{0}^{+\infty}\sin x^2  \mathrm{d}x=\int_{0}^{+\infty}\frac{\sin t}{2\sqrt{t}}  \mathrm{d}t
$$