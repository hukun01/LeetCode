# 96. Unique Binary Search Trees
class Solution:
    def numTrees(self, n: int) -> int:
        '''
        Let f(x, y) be the number of BSTs whose root is x, values are up to y;
        Let g(n) be the number of BSTs within [1, n];
        then f(x, y) = g(x-1) * g(y-x);
            Note that g(x-1) instead of g(x) because x is the root.
        and g(x) = sum(f(i, x) for i in [1, x])
        g(0) = 1, g(1) = 1, note that g(0) = 1 because null is a BST as well.
        We are looking for g(n).
        In terms of calculation, we need to start with the lower index,
        since the value of g(n) depends on the values of g(0) … g(n-1).
        '''
        g = [0] * (n + 1)
        g[0] = 1
        for x in range(1, n+1):
            g[x] = sum(g[i-1] * g[x-i] for i in range(1, x+1))
        return g[n]