class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        '''
        Union Find.
        '''
        N, W = len(A),len(A[0])
        A = set(A)
        def similar(w1, w2):
            return sum(c1 != c2 for c1, c2 in zip(w1, w2)) == 2
        
        uf = { w: w for w in A }
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        def union(x, y):
            uf[find(x)] = find(y)
        for a in A:
            find(a)
            if len(a) >= N:
                [union(a,b) for b in A if similar(a,b)]
            else:
                for i in range(W - 1):
                    for j in range(i + 1, W):
                        b = a[:i] + a[j] + a[i+1:j] + a[i] + a[j+1:]
                        if b in A:
                            union(a, b)
        return len({find(key) for key in uf})