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

**The ooperation on NSG:** Define '$\cdot $':
$$
Ha\cdot Hb=H(ab)
$$