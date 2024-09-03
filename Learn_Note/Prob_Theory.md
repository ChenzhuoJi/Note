# Chapter Ⅰ：Combinatorial Analysis

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
