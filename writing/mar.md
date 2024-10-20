$$
P(A)=\binom{n}{k}\left[ \frac{\lambda t}{n}+o(\frac{t}{n}) \right]^k\left[ 1- \frac{\lambda t}{n}-o(\frac{t}{n})  \right] ^{n-k}
$$
其中有 $\displaystyle n^k\left[\frac{\lambda t}{n}+o(\frac{t}{n}) \right]^k=\lambda t+t(\frac{o(t/n)}{t/n})\to \lambda t $，$\displaystyle X\left[\frac{\lambda t}{n}+o(\frac{\lambda t}{n})  \right]^{n-k}$ 
$$
P(N(t)=k)=P(A)\sim e^{-\lambda t}\frac{(\lambda t)^k}{k!}
$$
$\mathrm{d}$

$$
P(F_1|E)=\binom{7}{5}p^5(1-p)^2
$$
$$
P(F_2|E)=\binom{7}{5}p^5(1-p)^2
$$
对于任意的 $\epsilon>0$，都存在正整数 $N$，对于任意正整数 $p$ 以及任意的 $x\in I$，满足：
$$
\left| \sum_{k=n+1}^{n+p}\alpha_{k}(x) \right| =|\alpha_{n+1}(x)+ \cdots \alpha_{n+p}(x)|<\epsilon
$$

令$ R=\{选取到的小球是红色\}, G=\{选取到的小球是绿色\},B=\{选取到的小球是黑色\}$
$$
P(X=0)=\frac{1}{3}\left[ P(X=0|R)+P(X=0|G)+P(X=0|B) \right] =\frac{1}{3}\left[ \frac{\displaystyle \binom{15}{4}}{\displaystyle \binom{25}{4}}+\frac{\displaystyle \binom{17}{4}}{\displaystyle \binom{25}{4}}+\frac{\displaystyle \binom{18}{4}}{\displaystyle \binom{25}{4}}\right] 
$$

以选取到的颜色是红色作为条件：
$$
P(X_1=1|R)=\frac{\displaystyle \binom{10}{1}}{\displaystyle \binom{25}{1}}=\frac{10}{25}
$$
$$
P(X_2=1|R)=\frac{\displaystyle \binom{10}{1}\binom{9}{1}}{\displaystyle \binom{25}{1}\binom{24}{1}}+\frac{\displaystyle \binom{15}{1}\binom{10}{1}}{\displaystyle \binom{25}{1}\binom{24}{1}}=\frac{10}{25}
$$
$$
P(X_3=1|R)=\frac{\displaystyle \binom{10}{1}\binom{9}{1}\binom{8}{1}+\binom{10}{1}\binom{15}{1}\binom{9}{1}+\binom{15}{1}\binom{10}{1}\binom{9}{1}+\binom{15}{1}\binom{14}{1}\binom{10}{1}}{\displaystyle \binom{25}{1}\binom{24}{1}\binom{23}{1}}=\frac{10}{25}
$$
$$
P(X_4=1|R)=\frac{\binom{10}{1}\binom{9}{1}\binom{8}{1}\binom{7}{1}+\binom{10}{1}\binom{15}{1}\binom{9}{1}\binom{8}{1}+\binom{15}{1}\binom{10}{1}\binom{9}{1}\binom{8}{1}+\binom{15}{1}\binom{14}{1}\binom{10}{1}\binom{9}{1}+\binom{15}{1}\binom{14}{1}\binom{13}{1}\binom{10}{1}+\binom{15}{1}\binom{10}{1}\binom{14}{1}\binom{9}{1}}{ \binom{25}{1}\binom{24}{1}\binom{23}{1}\binom{22}{1}}=\frac{10}{25}
$$
同理可以得到:
$$
P(X_i=1|G)=\frac{7}{25}
$$
$$
P(X_i=1|B)=\frac{8}{25}
$$

$P(X_i=1)=\frac{1}{3}(\frac{10+7+8}{25})=\frac{1}{3}$

$$
P(X=1)=\frac{1}{3}\left[ P(X=1|R)+P(X=1|G)+P(X=1|B) \right] 
$$

$X=X_1+X_2+X_3+X_4$
$E(X)=E(X_1)+E(X_2)+E(X_3)+E(X_4)=\frac{4}{3}$




$$
\begin{aligned}
P(X=n+k|X>n) & = \frac{P(X=n+k,X>n)}{P(X>n)}  \\
& = \frac{\displaystyle (1-p)^{n+k-1}p}{\displaystyle 1-\sum_{k=1}^{n-1}(1-p)^{k-1}p}  \\
& = \frac{\displaystyle (1-p)^{n+k-1}p}{\displaystyle 1-\frac{1-(1-p)^{n-1}}{1-(1-p)}p}  \\
& = (1-p)^kp  \\
& = P(X=k)  \\
\end{aligned}
$$

$Y=n,n+1,n+2, \ldots ,N$，Y等于 i 说明比 i 大的 N-i 个数没有被选中，并且 i 被选中了。设 $E_i=\{ i 被选中\}$，$F_i=\{后 N-i 个数没有被选中\}$
$$
P(Y=i)=P(E_i F_i)=P(E_i|F_i)P(F_i)=\frac{\displaystyle \binom{i-1}{n-1}}{\displaystyle \binom{i}{n}}\frac{\displaystyle \binom{i}{n}}{\displaystyle \binom{N}{i}}=\frac{\displaystyle \binom{i-1}{n-1}}{\displaystyle \binom{N}{i}}
$$

$$
E(Y)=\sum_{i=n}^{N}\frac{i\displaystyle \binom{i-1}{n-1}}{\displaystyle \binom{N}{i}}
$$

设第 i 次取到的球是红球事件为 $R_i$，$\displaystyle P(X=i)=P(R_1R_2\cdots R_{i-1}R_i)=\frac{1}{2}\times \frac{2}{3}\times \frac{3}{4}\times \cdots \frac{i-1}{i}\times \frac{1}{i+1}=\frac{1}{i(i+1)}$
$$
\begin{aligned}
P(X >i) & = 1-P(X\le i)  \\
& = 1-\sum_{k=1}^{i}\frac{1}{k(k+1)}  \\
& =\frac{1}{k+1}
\end{aligned}
$$

$$
P(X< \infty)=\lim_{n \to \infty}P(X\le n)= \lim_{n \to \infty}(1-\frac{1}{n+1})=1
$$

$$
E(X)=\sum_{i=1}^{\infty}\frac{1}{i+1}\to \infty
$$
