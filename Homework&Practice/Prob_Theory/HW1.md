**Problem.1**

(a): There are 26 letters and 10 numbers for each place. So the number is $26^2\times 10^5$

(b): This is a permutation problem. The number is $A_{26}^2* A_{10}^5$

**Problem.2**

(a): $A_8^8=8!$

(b): See A & B as a whole.Then the row includs 7 "persons" and there are $A_2^2$ arrangements in A&B. The final anwser is:  
$$
A_7^7\times A_2^2
$$

(c): First we put the men in a row, and then put women in the gaps of men(both ends can also be placed).
$$
A_4^4\times C_5^4\times A_4^4
$$

(d): Like (b), the anwser is $A_5^5\times A_4^4$ . 

(e): $(A_2^2)^4\times A_4^4$

**Problem.3**

$
\begin{aligned}
(3x^2+y)^5 & = (3x^2)^5+5(3x^2)^4y+10(3x^2)^3y^2+10(3x^2)^2y^3+5(3x^2)y^4+y^5  \\
& = 243x^{10}+405x^{8}y+270x^{6}y^{2}+90x^4y^3+15x^2y^4+y^5  \\
\end{aligned}
$

**Problem.5**
Considering $(x_1+x_2+ \cdots +x_r)^n$, the cofficient of $x_1^{n_1}x_2^{n_2}\cdots x_r^{n_r}$ is $\displaystyle \binom{n}{n_1\ n_2\ \cdots\ n_r}$.We choose the term with the method as follows:
1. choose $x_1$ first,and then choose $x_1^{n_1-1}x_2^{n_2}\cdots x_r^{n_r}$, its confficient is $\displaystyle \binom{n-1}{n_1-1 \ n_2 \cdots\ n_r}$
2. choose $x_2$ first,and then choose $x_1^{n_1-1}x_2^{n_2}\cdots x_r^{n_r}$, its confficient is $\displaystyle \binom{n-1}{n_1 \ n_2-1 \cdots\ n_r}$

......, repeat this method until choose all $x_i$. The final cofficient is $\displaystyle \binom{n-1}{n_1-1\ n_2\ \cdots\ n_r}+\binom{n-1}{n_1\ n_2-1\ \cdots\ n_r}+ \cdots +\binom{n-1}{n_1\ n_2\ \cdots\ n_r-1}=\binom{n}{n_1\ n_2\ \cdots\ n_r}$

**Problem.6**

(a): $\displaystyle \binom{10}{6}$

(b): $\displaystyle \binom{10}{3}\binom{7}{3}$

**Problem.7**

According the collary of pigionhole principle, $\displaystyle \left\lceil \frac{200}{6} \right\rceil =34$. That shows that anyone of these classes should give 34 positions at least.

**Problem.8**

|$EF$|$E\cup F$|$FG$|$EF^c$|$EFG$|
|---|-------|---|---|---|
|one of two dice lands on 1,and the other one lands on an even number|one of dices lands on 1 or the sum of dice is odd|one lands on 1 and the other one lands on 4|the sum of dice is odd and 1 doesn't occur in two tosses|(same as $EF$) one of two dice lands on 1,and the other one lands on an even number|

**Problem.9**

(a): sample space: $\{ 0g,0f,0s,1g,1f,1s \}$ (0g represents that the patient has no insurance and is rated as good,other notions are similar)

(b): $A$: $\{ 0s,1s \}$

(c): $B$: $\{ 0g,0f,0s \}$

(d): $B^c\cup A$: $\{ 1g,1f,1s,0s \}$

**Problem.10**