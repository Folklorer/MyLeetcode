# 记录

#### 24.07.30   P2961  快速幂

对$x^{64}$的计算：不必用x乘63个x，可以考虑使用$x \rightarrow x^2 \rightarrow x^4 \rightarrow ... \rightarrow x^{64}$

计算 $x^n$，递归地计算出 $y = x^{\lfloor n/2 \rfloor}$，若n为偶数， $x^n = y^2$，若n为奇数，$x^n = y^2 \times x$

Python的 $ pow(x,y,z)=x**y\%z $ 就是快速地求幂方法

