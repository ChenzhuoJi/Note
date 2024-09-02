## *Abstract Algebra*
### Group.1

Prove *Euler Theorem* : $a,\varphi$ are two coprime integers.Let $\varphi(n):$The number of integers that less than $n$ and coprime with $n$
Then $a^{\varphi(n)}\equiv 1(mod\ n)$

**Proof:**
First, we give *G*={m|m is the integers less than & coprime with $n$}.And $'\cdot'$ definited in $G$.
$|G|=\varphi(n)$
$$
a,b\in G,a\cdot b=m\in G,ab\equiv m(mod\ n)
$$
Because a,b are coprime with n,then ab is coprime with n,too.
$$
ab=qn+m
$$
So $m$ is coprime with $n$,$m\in G$
***
*Lagrange Theorem* : *The order of subgroup is the factor of $|G|$*
*Theorem.1* : The infinite group $G$ and its element a,a have its cycle N : $a^N=e$
*Corollary.1* : $H=${$a,a^2,a^3,\dotsb,a^N=e$},then $H$ is a subgroup of $G$.$|H|=N$,So $N|o(G)\Rightarrow a^{|G|}=e$
***
We come back to the a in the question and G definited.$a$ is comprime with n,if a is less than n ,then a is in G.On the other hand, if a isnot less than n,we consider b:
$$
b\equiv a(mod\ n),b^M\equiv a^M(mod\ n)
$$
b is in G.According to *Corollary.1*,we can easily conclude that with the operation "$\cdot$" definited :
$$
a^{\varphi(n)=|G|}=b^{|G|}=e=1
$$
***
### Group.2
#### Normal Group
**Definition 2.1:** *A subgroup H is normal,if Ha=aH, $\forall$ a $\in$ G,noted as $H\lhd G$*
**Proposition 2.1:** *H is a subgroup of G,$H\lhd G\Leftarrow \forall h\in H $ and $g \in G,ghg^{-1}\in H$*
**Proof:** 
$ghg^{-1} \in H$,says that $\exist h_1 \in H,ghg^{-1}=h_1\Rightarrow gh=h_1g$,showing $\forall ah_1\in aH,\exist h_2a\in Ha,s.t\ ah_1=h_2a$

**The ooperation on NSG:** 
Define '$\cdot $':
$$
Ha\cdot Hb=H(ab)
$$
首先，我们需要先保证这个运算在集合H上时*be definable*的，H是正规子群，所以$Ha=aH$
***
商集：一个集合和一个在集合上defined的等价关系 '$\diamond $' 决定，一个等价关系和一个元素组合会导出与此元素等价的所有元素，，将这些导出元集成到一个集合称作等价类。

**Ex.1:** 我们考虑整数集，定义等价：$a \diamond b \Leftrightarrow a\equiv b(mod\ 3) $,我们就可以导出所有等价类到一个集合:$\{[1],[2],[0]\}$
**Ex.2** 我们考虑集合：$\{(x,y)|x^2+y^2=1 \}$,$(a_1,b_1)\diamond (a_2,b_2)=:a_1=-a_2,b_1=-b_2$,这样同一直径上的两个点就是一个等价类，这样$\frac{1}{2}$圆的数量的“两点合集”就是等价类集合即为商集
***
商群来自于右傍集的可划分性，因为存在等价关系：$a\diamond b=:Ha=Hb$，根据这种等价关系导出来了商集:$\bar{G}=\{Ha_1,Ha_2,\dots Ha_n\}$。(事实上这几个集合的阶数相同，也就*Largrange Theorem*的理论)
***
回到原来的讨论中，正规子群也是子集，有其对应的右傍集划分全集法，我们说正规子群对应的商集可以定义一种运算，使它具有群的性质。下面开始我们的讨论：
**一个运算：** 事实上二元运算是有序集合数对到单一集合上的映射$S\times S \rightarrow S$，要想称作运算（映射），其充要条件是：$$\cdot: S\times S \rightarrow S$$,$$(a,b)\rightarrow \cdot \ (a,b)$$ $a\in S,b\in S,\exist!\ c\in S,c=a\cdot b$
***
沿着这个思路，只需证明 '$\times$':$Ha\times Hb\rightarrow H(ab)$

$e:$  $He\times Ha=H(ae)=Ha$, $He$是幺元
$a^{-1}:$ $a,a^{-1}\in G,Ha^{-1}\times Ha=He$ 
$H(ab)$: $a_1,b_1\in G,a_1b_2\in G$ 

假设有这样与$a_1,b_1$不同的$a,b$，$Ha=Ha_1=aH=a_1H,Hb=Hb_1=bH=b_1H$,接下来说明：$H(a_1b_1)=H(a_2b_2)$,$H$是正规子群,我们需要反复利用其可交换的特性

一方面：
$$
\forall h\in H,\exist h_1\in H,hab=abh_1\Rightarrow \exist h_2\in H,hab=ah_2b_1\Rightarrow \exist h'\in H,hab=h'a_1b_1 
$$
以此类推，另一方面：
$$
\forall h'\in H,\exist h\in H,h'a_1b_1=hab
$$
故：$H(ab)=H(a_1b_1)$
***
**同态 & 同构**
同构和同态说的是一个映射$f:G_1\rightarrow G_2$,有以下性质：$a\in G_1,b\in G_2$
$$
f(a\cdot b)=f(a)f(b)
$$
我们可以从以往学的的例子中看出同态的关系：
* $(P^n,+)$，$A$是矩阵，$A(a+b)=Aa+Ab$
* $f(x),g(x)\in CR$，以及加法运算：$+$，映射：$\frac{d}{dx}$,$(f+g)'=f'+g'$
* $P$是可逆矩阵，映射：$f(A)=P^{-1}AP$，$f(AB)=f(A)f(B)$

根据同态映射$f$进行分类：
* $f$是单射，又称单同态。
* $f$是满射，称之为满同态，又称映上同态。
* $f$是双射，称之为同构。

**同态的性质**
1. $f(e),e$分别是$G_2,G_1$的幺元。
2. $f(x^{-1})=f(x)^{-1}$
3. $f(G_1)(ImG_1)$是$G_2$的子群
4. $Ker\ f=\{x\in G_1|f(x)=e'\}$是$G_1$的正规子群
5. 同构是等价关系。