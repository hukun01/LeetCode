# 959. Regions Cut By Slashes
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        '''
        Treat every cell as two parts a and b, and there are
        totally N*N*2 parts in the grid.
        A cell can be "a/b" or "b\a" or blank. We split it in
        this way so that we can use the same reference 'b' to
        connect to the neighbor at the next row.

        1. If the cell is blank, a connects to b;
        2. If the cell is '/', b connects to b's right part;
        3. If the cell is '\', a connects b's right part.

        And b always connects to its neighbor at the next row.
        '''
        N = len(grid)
        uf = [0] + [i for i in range(1, N * N * 2 + 1)]
        
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        def union(a, b):
            pA = find(a)
            pB = find(b)
            if pA != pB:
                uf[pA] = pB
                
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                a = (r * N + c) * 2 + 1
                b = a + 1
                if cell == ' ':
                    union(a, b)
                if c < N - 1:
                    x = b if cell == '/' else a
                    y = b + 1 if row[c + 1] == '/' else b + 2
                    union(x, y)
                if r < N - 1:
                    union(b, a + 2 * N)

        return sum(uf[i] == i for i in range(1, len(uf)))