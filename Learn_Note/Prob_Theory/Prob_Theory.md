# Chapter I：Combinatorial Analysis

## Counting

### Basic Counting Principles

**Theorem 1.1 (Pigeonhole principle. Dirichlet, 1834)**
if $n$ items are to be put into $m$ containers, with $n > m$,then at least one container must contain more than one item.

**Corollary 1.2:**
if $n$ items are to be put into $m$ containers, with $n > m$,then at least one container must contain at least $\left\lceil \frac{n}{m} \right\rceil$ item.

---

**example**:you go to a restaurant. That day, they propose 4 starters, 4 coursesand 3 desserts. You choose one starter, one course and one dessert to forminto your meal set. How many different sets are possible?

**answer**: $4 \times 4 \times 3 = 48$.

thus, we can get the following Proposition.

**Proposition 1.3:**
If $r$ experiments are to be performed sequentially(按顺序) and the first experiment can be performed in $n_1$ ways, . . . , the rth experiment in $n_r$ ways, then there are$\prod _{i = 1}^n n_i
$ ways to perform the $r$ experiments.

**example bis**:Still for the meal selection, you can either choose one starter andone course, or one course and one dessert. That is, you cannot take a starter,a course and a dessert. How many different sets are possible?
**answer**: $4 \times 4 + 4 \times 3 = 28$.

---

## Permutations

let's begin with an example:How many different ranking orders are possible for 10 tennis players? $A_{10} ^{10}$.

**Definition 1.4 (Permutation):**
An ordered ranking of $n \in  N^*$ distinct elements is called a **permutation**.

**Proposition 1.5:**
There are $n(n − 1)· · · 1$ permutations of $n \in  N^*$ distinct elements.

$$
P_1E_1P_2P_3E_2R = \frac{A_6^6}{A_2^2 \times A_3^3}
$$

组合：

## Combinations

## Multinomials

consider:

$$
(x_1 + x_2 + \cdots + x_r)^n
$$

for $x_1 ^{n_1}x_2 ^{n_2}\cdots x_r ^{n_r}$， we choose $n_1$'s $x_1$ in $n$ item, and $n_2$'s $x_2$ in $n-n_1$ item.

**Prop:**$n_1+n_2+n_3+\cdots +n_r=n$ have $(^{n+r-1}_{\ \ \ r-1})$ distinct nonnegative integer_valued vectors $(n_1,n_2,\cdots,n_r)$

**Proof:** We can see this problem as the form following:

$$
y_1+y_2+\cdots+ y_r=n+r
$$

where $y_i=n_i+1,y_i\ge 1$.Specifically,what we need to anwser is how many methods of inserting $r-1$ spacers in $n+r-1$ gaps.
**Ex:** $n=1,r=3$

$$
\bigcirc| \bigcirc| \bigcirc \bigcirc:(0,0,1)
$$

$$
\bigcirc| \bigcirc \bigcirc| \bigcirc:(0,1,0)
$$

$$
\bigcirc \bigcirc| \bigcirc| \bigcirc:(1,0,0)
$$

**i.e.** $(^{1+3-1}_{\ \ \ 3-1})=(^3_2)=3$

---

# Chapter.II Axioms of Probability

*2024/9/5*

## Set

**Definition 2.1**

1. random experiment
2. sample space (is denoted by $S$)
3. sample point

*Remark 2.2* $S$ can be finite or **infinite** (conutable or uncountable)

**Definition 2.2**
**subset/superset**

**Definition 2.3**
**event**

*Remark 2.3* Sure set: $S$, impossible set : $\empty$

**Relation**

1. Union
2. Intersection
3. Countable union/intersection
4. Mutually exclusive: $E\cap F=\empty$
5. Complement: $E^c$
6. Difference: $E\setminus F$
7. Symmertric difference: $E\triangle F=\{ \omega|\omega\in E\setminus F \ \rm{or}\  \omega\in F\setminus E \}$

**Proposition 2.5** (*De Morgan's Law*)

$$
(\bigcup_{i=1}^{n}E_i)^c=\bigcap_{i=1}^{n}E_i 
\\
(\bigcap_{i=1}^{n}E_i)^c=\bigcup_{i=1}^{n}E_i
$$

## Axioms of Probability

### Some Properties

$$
\mathbb{P}(\empty)=0
$$

**Proof** If we consider a sequence $\{ E_i \}$ where $	2E_1=S,E_i=\empty,\text{for}\ i\ge 2$,then $\displaystyle S=\bigcap_{} E_i$.Hence,

$$
\mathbb{P}(S)=\mathbb{P}(\bigcup_{i=1}^{\infty} E_i)=\sum_{i=1}^{\infty}\mathbb{P}(E_i)=\mathbb{P}(S)+\sum_{i=2}^{\infty}\mathbb{P}(E_i)\implies \mathbb{P}(\empty)=0
$$

$$
\mathbb{P}\left( \bigcup_{i=1}^{n}E_i \right)=\sum_{i=1}^{n}\mathbb{P}(E_i)
$$

where $E_i.E_j,i\not=j$ are mutually exclusive

**Proof** Similar to **Proof.1**

$$
\mathbb{P}(E)\le \mathbb{P}(F)
$$

where $E \subseteq F \subseteq \mathcal{A} $

**Proof** $\displaystyle \mathbb{P}(F)=\mathbb{P}(E+F\setminus E)=\mathbb{P}(E)+\mathbb{P}(F\setminus E)$

4. (inclusion and exclusion indentity) For any two events $E,F$

$$
\mathbb{P}(E \cup F)=\mathbb{P}(E)+\mathbb{P}(F)-\mathbb{P}(E\cap F)
$$

$$
\mathbb{P}\left (\bigcup_{i=1}^{n}E_i \right )=\sum_{k=1}^{n}(-1)^{k-1}\sum_{1\le i_1 \le i_2\le \cdots\le i_k\le n}\mathbb{P}(E_{i_1}\cap E_{i_2}\cdots \cap E_{i_k})\tag{2.1}
$$

**Proof** $\mathbb{P}(E\cup F)=\mathbb{P}(E\cup E^cF)=\mathbb{P}(E)+\mathbb{P}(E^cF)$,

consider $EF+E^cF=F,EF\cap E^cF=\empty \implies \mathbb{P}(E)+\mathbb{P}(E^cF)=\mathbb{P}(E)+\mathbb{P}(F)-\mathbb{P}(EF)$

**Ex** $n=4$:

$$
\begin{aligned}
&\mathbb{P}\left( \bigcup_{i=1}^{4}E_i \right)\\
&=\mathbb{P}(E_1)+\mathbb{P}(E_2)+\mathbb{P}(E_3)+\mathbb{P}(E_4)\\
&-\mathbb{P}(E_1E_2)-\mathbb{P}(E_2E_3)-\mathbb{P}(E_2E_4)-\mathbb{P}(E_1E_4)-\mathbb{P}(E_1E_3)-\mathbb{P}(E_3E_4)\\
&+P(E_1E_2E_3)+\mathbb{P}(E_1E_3E_4)+\mathbb{P}(E_1E_2E_4)+\mathbb{P}(E_2E_3E_4)\\
&-\mathbb{P}(E_1E_2E_3E_4)
\end{aligned}
$$

$$
\mathbb{P}(E\cup F)\le \mathbb{P}(E)+\mathbb{P}(F)
$$

(A gerneralization) For a finite sequence of events $E_1,E_2, \ldots ,E_n$

$$
\mathbb{P}\left( \bigcup_{i=1}^{n}E_i  \right)\le \mathbb{P}(E_1)+\mathbb{P}(E_2)+ \cdots \mathbb{P}(E_n) \tag{2.2}
$$

(Infinite) *Bool's inequality* : For a countably infinite sequence of events $\{ E_i \}_{i\ge 1}$

$$
\mathbb{P}\left( \bigcup_{i=1}^{\infty}E_i \right)\le \sum_{i=1}^{\infty}\mathbb{P}(E_i)
$$

**Proof (2.2)** Note the identity:

$$
\bigcup_{i=1}^{n}E_i=E_1+E_1^cE_2+ \cdots +E_1^cE_2^c\cdots E_{n-1}^cE_n
$$

or this form:

$$
F_1=E_1\\
F_2=E_2\setminus E_1\\
\vdots\\
F_k=E_k\setminus\bigcup_{i=1}^{k} E_i \\
$$

$$
\mathbb{P}\left( \bigcup_{i=2}^{n}E_i\right )=\mathbb{P}(E_1)+\sum_{i=1}^{n}\mathbb{P}(E_1^cE_2^c\cdots E_{i-1}^c E_i)
$$

denote $E_1^cE_2^c\cdots E_{i-1}^c E_i=B_i$, where $\mathbb{P}(B_i)\le \mathbb{P}(E_i)$.Thus,

$$
\mathbb{P}\left( \bigcup_{i=1}^{n}E_i  \right)\le \mathbb{P}(E_1)+\mathbb{P}(E_2)+ \cdots \mathbb{P}(E_n)
$$

### Ex 2.1

---

*2024/9/10*

### Continue Properties

**Definition** Increasing/Decreasing sequence $\{ E_n \}$, we ***define a new event*** $\displaystyle \lim_{n \to \infty}E_n$ by $\displaystyle \lim_{n \to \infty}E_n=\bigcup_{n=1}^{\infty}E_n$

5. For decreasing/increasing sequence $E_n$

$$
\lim_{n \to \infty}\mathbb{P}(E_n)=\mathbb{P}(\lim_{n \to \infty}E_n)
$$

We prove the case for increasing sequence $\{ E_n \}$

$$
RHS=\mathbb{P}(\bigcup_{n=1}^{\infty}E_n)=\mathbb{P}(\bigcup_{n=1}^{\infty}F_n)=\sum_{n=1}^{\infty}\mathbb{P}(F_n)=\lim_{n \to \infty}\sum_{k=1}^{n}\mathbb{P}(F_n)=\lim_{n \to \infty}\mathbb{P}(E_n)=LHS
$$

### Ex 2.2

Suppose we have an infinitely large urn, and an infinite collection of balls labled as number 1,2,3,4,...

* At 1 min to 12p.m., balls numbered 1 through 10 are placed in the urn and a ball is randomly selected and withdrawn.
* At $\frac{1}{2}$ min to 12p.m., balls numbered 11 through 20 are placed in the urn and a ball is randomly selected and withdrawn.
* At $\frac{1}{4}$ min to 12p.m., balls numbered 21 through 30 are placed in the urn and a ball is randomly selected and withdrawn.

and so on. How many balls are there in the urn at 12pm.

**Proof** Consider $1^{th}$ ball, denote event $\{1^{th}\ \text{ball is still in the urn at }\ \frac{1}{2^k}\ \text{min to 12pm} \}$ as $E_k$, and event $\{ 1^{th}\ \text{ball is in the urn at 12pm}\}$ as E
apparently,

$$
E_n \subseteq \cdots E_2 \subseteq E_1
$$

$$
\begin{aligned}
\mathbb{P}(E) & = \lim_{n \to \infty}\mathbb{P}(\bigcup_{k=1}^{n}E_k)  \\
& = \lim_{n \to \infty}\mathbb{P}(E_n)  \\
& = \lim_{k \to \infty}\frac{9}{10}\frac{18}{19}\frac{27}{28}\cdots \frac{9k}{9k+1}  \\
& = \exp(\sum_{k=1}^{\infty}\ln (1-\frac{1}{9k+1}))\to 0  \\
\end{aligned}
$$

Similarly, the event $\{ i^{th}\ \text{is in the urn at 12pm}\}$, denoted by $F_i$, $\mathbb{P}(F_i)=0$.

$\{ \text{the urn is not empty} \} \Leftrightarrow \{ \text{there is at least one ball in the urn} \}$. Finally, the urn is empty.

## Uniform Probability measure on finite sample

### Poker Problem

52 cards to 4 people. What is the probability that

* one of the players recieves all 13 spades. $(E_1)$
* each player recieves 1 ace. $(E_2)$

(1)

$$
\mathbb{P}(E_1)=\frac{|E|}{|S|}=\cfrac{\binom{39}{13\ 13\ 13}}{\binom{52}{13\ 13\ 13\ 13}}
$$

(2)

$$
\mathbb{P}(E_2)=\frac{\binom{4}{1\ 1\ 1\ 1}\binom{48}{12\ 12\ 12\ 12}}{\binom{52}{13\ 13\ 13\ 13 }}
$$

### Birthday Problem

### The Matching Problem

Each of N men throw his hat into the center of room, and the hats are first mixed up. Then each man randomly selects a hat. What is the probability that none of the men selects his own hat?

**Solution** Denote the event 'the $i^{th}$ man gets his hat' as $E_i$. According to *Inclusive&Exclusive Theorem*

$$
\mathbb{P}(\bigcup_{i=1}^{N}E_i)=\sum_{i=1}^{N}\mathbb{P}(E_i)-\sum_{1\le i_1,i_2\le N}\mathbb{P}(E_{i_1}E_{i_2})+ \cdots +(-1)^{k-1}\sum_{1\le i_1,i_2, \ldots ,i_k \le N}\mathbb{P}(E_{i_1}E_{i_2}\cdots E_{i_k})+ \cdots +(-1)^{N-1}\mathbb{P}(E_1E_2\cdots E_N)
$$

note that

$$
\mathbb{P}(E_{i_1}E_{i_2}\cdots E_{i_k})=\frac{(N-k)!}{N!}, \binom{N}{k}\frac{(N-k)!}{N!}=\frac{1}{k!}
$$

then

$$
\mathbb{P}(\bigcup_{i=1}^{N} E_i)=1-\frac{1}{2!}+\frac{1}{3!}+ \cdots +(-1)^{N-1}\frac{1}{N!}
$$

The event "none of men selects his own hat" and $E$ is complemenatary.

# Charpter III

## Conditional Probability (obeserve and predict)

$$
\mathbb{P}(E|F)=\frac{\mathbb{P}(E\cap F)}{\mathbb{P}(F)}
$$

### $P(\cdot |F)$ as a probability measure

Use three axioms to prove

**Prop 3.3** The function mapping $\mathbb{P}_F$: $A\to \mathbb{R}$ defined by $\mathbb{P}_F(E)=\mathbb{P}(E|F)$ is a probability measure on $(S,A)$

**Prop 3.4** Let F be an event with $\mathbb{P}(F)>0$, the conditional probability of event $E\in A$ given that $F$ has occurred can be computed as:

$$
\mathbb{P}(E|F)=\frac{|E\cap F|}{|F|}
$$

**Prop 3.5** (*Mutiplication Rule*) Let $E_1,E_2, \ldots ,E_n$ be a sequence of $n\in \mathbb{N}, n\ge 1$ events. Then we have:

$$
\mathbb{P}(\bigcap_{i=1}^{n}E_i)=\mathbb{P}(E_1)\mathbb{P}(E_2|E_1)\mathbb{P}(E_3|E_1\cap E_2)\cdots \mathbb{P}(E_n|\bigcap_{i=1}^{n-1} E_i)
$$

**Proof** Expand $RHS$ and calcel out each other

### Example

**Example 3.1** (*Pocke game revisied*) 52 cards to 4 piles of 13 cards each. Compute the probability that each pile has exactly 1 ace.

**Solution**

Let $E_i$ be the event that ith pile have 1 ace

$$
\mathbb{P}(E_1E_2E_3E_4)=\mathbb{P}(E_1)\mathbb{P}(E_2|E_1)\mathbb{P}(E_3|E_1\cap E_2)\mathbb{P}(E_4|E_1\cap E_2\cap E_3)
$$

* $\displaystyle $

**Example 3.2** (*The matching problem revisited*) In matching problem, the probability that no matches occur when N people select from N mixed-up hats, denoted by $P_N$, is given by:

$$
P_N=\sum_{i=0}^{N}(-1)^i \frac{1}{i!}
$$

What is the probabiliy that exactly k of the N people have matches?

**Solution**

Let E be the event that $1,2, \ldots ,k$ have matches, and G be the event that no matches occur among people $k+1, \ldots N$

$$
\mathbb{P}(G|E)=P_{N-k}
$$

The probability that k of N people have matches is given by :

$$
\binom{N}{k}\mathbb{P}(E\cap G)
$$

$E$ is the event that the first $k$ people get their hats, which means $N-k$ hats permutate in $N-k$ people, i.e.

$$
|E|=(N-k)!
$$

$$
\mathbb{P}(E)=\frac{|E|}{N!}=\frac{(N-k)!}{N!}
$$

$$
\binom{N}{k}\mathbb{P}(E\cap G)=\mathbb{P}(E)\mathbb{P}(G|E)=\frac{N!}{(N-k)!k!}\frac{(N-k)!}{N!}P_{N-k}=\frac{1}{k!}P_{N-k}
$$

## Baye's Formula

### First Baye's fomula

$$
\mathbb{P}(F|E)=\frac{\mathbb{P}(E|F)\mathbb{P}(F)}{\mathbb{P}(E)}
$$

### Law of total probability

Let $\{ F_i \}$ be a countable **partition** of the sample space $S$

$$
\mathbb{P}(E)=\sum_{j=1}^{\infty}\mathbb{P}(E\cap F_j)
$$

with the knowledge of conditional probability,

$$
\mathbb{P}(E)=\sum \mathbb{P}(E|F_i)\mathbb{P}(F_i)
$$

In particular,

$$
\mathbb{P}(E)=\mathbb{P}(E|F)\mathbb{P}(F)+\mathbb{P}(E|F^c)(1-\mathbb{P}(F))
$$

### Example

**Example 3.3**

**Solution**

$$
\mathbb{P}(R_2)=\mathbb{P}(R_1)\mathbb{P}(R_2|R_1)+\mathbb{P}(R_2|R_1^c)\mathbb{P}(R_1^c)=\frac{r}{r+b}=\mathbb{P}(R_1)
$$

Then we prove that $\mathbb{P}(R_n)\equiv \mathbb{P}(R_1)$

Suppose it's true for $n$

$$
\begin{aligned}
\mathbb{P}(R_{n+1}) & = \mathbb{P}(R_{n+1}|R_n^c)\mathbb{P(R_n)}+\mathbb{P}(R_{n+1}|R_n^c)\mathbb{P}(R_n^c)  \\
& = \frac{r+s}{r+b+s} \frac{r}{r+b}+\frac{r}{r+b+s} \frac{b}{r+b}  \\
& = \frac{r}{r+b}  \\
\end{aligned}
$$

Let $(S,A,\mathbb{P})$ be a  probability space. Let $E\in A$ be an event labled as *success*, that occurs with probability p. Independent trials are performed. but the number of trials is **NOT** preset. <span class="code-inl">Let $X$ be the number of trials until the first success</span>, then $X$ is said to be a **geometric random variable** with parameter *p*. The pmf is given by
$$
p(n)=\mathbb{P}(X=n)=(1-p)^{n-1}p
$$

For the geometric random variable $X$ with teh parameter p: 

the distribution function is 
$$
F(k)=\mathbb{P}(X\le k)=1-(1-p)^k, k=1, 2, \cdots
$$

the expected value: 
$$
\mathbb{E}(X)=\frac{1}{p}
$$

the variance is:
$$
Var(X)=\frac{1-p}{p^2}
$$

## Negative binomial random variable

Let $(S,A,\mathbb{P})$ be a  probability space. Let $E\in A$ be an event labled as *success*, that occurs with probability p. Independent trials are performed until a total of *r* successes is accumulated. Let $X$ be the number of trials required, then $X$ is said to be a negative binomial random variable with parameter $(r,p)$

In particular, a geometric random variable is just a negative binomial r.v. with parameter $(1,p)$. 

The pmf of a negative binomial r.v. is given by
$$
P(X=n)=\binom{n-1}{r-1}p^r(1-p)^{n-r}
$$

## Poisson random variable

Let $(S,A,\mathbb{P})$ be a  probability space, $X$ is said to be a Poisson random variable with parameter $\lambda>0$ if its probability mass function is given by
$$
p(i)=\mathbb{P}(X=i)=e^{-\lambda}\frac{\lambda^i}{i!}
$$

### Poisson paradigm

We can weaken the condition of binomial random variable in the application of Poisson approx.

Consider *n* events, event *i* occurs with paobability $p_i, i=1,2,3,\cdots ,n$. If all $p_i$'s are small and the trial are either independent or at most "weakly dependent". The number