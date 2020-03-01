class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        '''
        Union Find.
        We need to put similar words in their groups with UF.

        We can either enumerate all the possible similar word with time N(W^3),
        or we can iterate through all the other words to find the similar ones with
        time (N^2)W.
        We can switch to different approaches depending on N > W^2 or not.
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
            if N <= W:
                [union(a,b) for b in A if similar(a,b)]
            else:
                for i in range(W - 1):
                    for j in range(i + 1, W):
                        b = a[:i] + a[j] + a[i+1:j] + a[i] + a[j+1:]
                        if b in A:
                            union(a, b)
        return len({find(key) for key in uf})