$$
P(E|F_1)=\binom{7}{5}p^5(1-p)^2
$$

4.60
$$
P(X=i)=e^{-5}\frac{5^i}{i!}
$$

4.66
$$
P(C_i)=\frac{\displaystyle \frac{A^2_2 A^{2n-1}_{2n-1}}{2n-1}}{\displaystyle \frac{A_{2n}^{2n}}{2n}}=\frac{2}{2n-1}
$$
$$
P(C_j|C_i)=\frac{P(C_j C_i)}{P(C_i)}= 2\frac{\displaystyle \frac{\displaystyle \frac{A_{2}^2\times A_{2}^2\times A_{2n-2}^{2n-2}}{2n-2}}{\displaystyle \frac{A_{2n}^{2n}}{2n}}}{\displaystyle \frac{\displaystyle \frac{A_2^2\times A_{2n-1}^{2n-1}}{2n-1}}{\displaystyle \frac{A_{2n}^{2n}}{2n}}}=\frac{2}{2n-2}
$$

$n$很大时, $C_i$ 和 $C_j$ 是弱相依事件，所以可以近似的认为这是 $n$ 个独立的事件。又因为 $n$ 很大，所以说我们考虑一个随机变量 $X$ , 代表有 $X$ 对夫妻坐在了一起，我们只需考虑 $P(X=0)$, 用参数 $\displaystyle \lambda=n\times \frac{1}{n-1}\to 1, n\to \infty$ 的泊松分布近似：
$$
P(X=0)=\frac{1}{1}e^{-1}=e^{-1}
$$
4.60
$$
P(C|E)=P(X=2)=e^{-3}\times \frac{9}{2!}=\frac{9}{2}e^{-3}
$$
$$
P(C|E^c)=e^{-5}\times \frac{25}{2!}=\frac{25}{2}e^{-5}
$$
$$
P(E|C)=\frac{P(C|E)P(E)}{P(C|E)P(E)+P(C|E^c)P(E^c)}=\frac{27\exp(-3)}{27\exp(-3)+25\exp(-5)}\cong 0.889
$$
4.75
让 $X$ 是强队系列赛胜利的比赛赛赛数，$ P(X=4)=(0.6)^4=0.1296 $，$ P(X=5)=\binom{4}{1}\times 0.4\times 0.6^4=0.20736 $，$ P(X=6)=\binom{5}{2}0.4^2\times 0.6^4=0.20736$，$P(X=7)=\binom{6}{2}0.4^3\times 0.6^4=0.165888$
$$
P_1(强队胜利)=0.710208
$$
在三局两胜赛之下，强队胜利的概率是：
$$
P_2(强队胜利)=0.6^2+0.6\times 0.6\times 0.4\times \binom{2}{1}=0.288=0.648
$$
4.79
<p> $1\le k<\min\left\{ N_1,N_2 \right\} $
$$
P(left:0,right:k)=\binom{N_1+N_2-k-1}{N_2}(\frac{1}{2})^{N_2-k}(\frac{1}{2})^{N_1-1}(\frac{1}{2})
$$
$$
P(left:k,right:0)=\binom{N_1+N_2-k-1}{N_2}(\frac{1}{2})^{N_1-k}+(\frac{1}{2})^{N_2-1}(\frac{1}{2})
$$
$$
P(X=k)=
$$
</p>

<p> $k\ge \min\left\{ N_1,N_2 \right\} $
$$
P=(\frac{1}{2})^{\max\left\{ N_1,N_2 \right\} }
$$
</p>

6.
<p>
$$
P(X=0)=\frac{\displaystyle \binom{94}{10}}{\displaystyle \binom{100}{10}}
$$
$$
P(X>2)=1-P(X=0,1)=1-\left( \frac{\displaystyle \binom{94}{10}}{\displaystyle \binom{100}{10}}+\frac{\displaystyle \binom{94}{9}\binom{10}{1}}{\displaystyle \binom{100}{10}} \right) 
$$
</p>

