# 96. Unique Binary Search Trees
class Solution:
    def numTrees(self, n: int) -> int:
        '''
        Use f(x) to denote the number of BSTs whose root is x;
        Use g(n) to denote the number of BSTs from 1...n;
        then f(x) = g(x-1) * g(n-x);
        and g(n) = f(1) + f(2) + ... + f(n);
        and g(x) = sum(f(i) for i in [1, x])
        g(0) = 1, g(1) = 1, note that g(0) = 1 because null is a BST as well.
        We are looking for g(n) = sum(g(x) for x in [1, x])
        In terms of calculation, we need to start with the lower number, 
        since the value of G(n) depends on the values of G(0) … G(n-1).
        '''
        g = [0] * (n + 1)
        g[0] = 1
        for x in range(1, n+1):
            g[x] = sum(g[i-1] * g[x-i] for i in range(1, x+1))
        return g[n]