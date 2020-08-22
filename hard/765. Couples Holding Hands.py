# 765. Couples Holding Hands
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        '''
        Union find.

        Each couple is a node in the graph. There are n nodes, n = len/2.
        If in position 2i and 2i+1, there are people from couple c1 and c2,
        the permutations will involve c1 and c2, so we connect them together.
        
        With the number k of connected components, we need n - k swaps to make
        them disjoint sets again.
        '''
        ans = 0
        n = len(row) // 2
        uf = [i for i in range(n)]

        def find(i):
            if i != uf[i]:
                uf[i] = find(uf[i])
            return uf[i]

        def union(a, b):
            pA = find(a)
            pB = find(b)
            if pA != pB:
                uf[pA] = pB

        for i in range(n):
            a = row[2 * i]
            b = row[2 * i + 1]
            union(a // 2, b // 2)

        return n - sum(i == uf[i] for i in range(n))