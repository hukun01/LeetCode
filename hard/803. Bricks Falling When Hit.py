# 803. Bricks Falling When Hit
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        '''
        UnionFind.
        We need to check the connectivity between cells, so UnionFind comes to
        mind naturally. However, UnionFind doesn't deal with removing edge.
        The key is to process 'hits' reversely - instead of removing bricks in
        hits, we add the bricks back, and measure how many bricks are added to
        the roof.
        We copy the original grid into a new grid 'A', and set all the hit
        bricks to 0.
        Then use a special brick 'R * C' as the roof, and build a UF using
        bricks in A (with hit bricks set to 0).
        Now we reversely iterate through 'hits', if the brick in the original
        grid is 0, we skip it. Otherwise, we are adding a brick to 'A', we need
        to check how many new bricks would be added to roof due to new edge.

        Also note that when we compute the size of roof component, we need to
        minus one to exclude the special nonexistent brick.

        Time: O(n) where n is the number of elements. And if we treat reverse
              Ackerman function as O(1), which is the amortized time complexity
              of UF operations.
        Space: O(n).
        '''
        R, C = len(grid), len(grid[0])
        def index(r, c):
            return r * C + c
        
        def neighbors(r, c):
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        uf = UnionFind(R * C + 1)

        A = [row[:] for row in grid]
        for r, c in hits:
            A[r][c] = 0

        ROOF = R * C
        ans = []
        for r in range(R):
            for c in range(C):
                if A[r][c] == 0:
                    continue
                cur = index(r, c)
                if r == 0:
                    uf.union(cur, ROOF)
                if r - 1 >= 0 and A[r-1][c] == 1:
                    uf.union(cur, index(r - 1, c))
                if c - 1 >= 0 and A[r][c-1] == 1:
                    uf.union(cur, index(r, c - 1))

        ans = []
        for r, c in reversed(hits):
            if grid[r][c] == 0:
                ans.append(0)
                continue

            pre_roof = uf.roof_size(ROOF)
            cur = index(r, c)
            for nr, nc in neighbors(r, c):
                if A[nr][nc]:
                    uf.union(cur, index(nr, nc))
            if r == 0:
                uf.union(cur, ROOF)
            A[r][c] = 1
            ans.append(max(0, uf.roof_size(ROOF) - pre_roof - 1))

        return ans[::-1]


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def roof_size(self, x):
        return self.size[self.find(x)] - 1

    def union(self, x, y):
        x0 = self.find(x)
        y0 = self.find(y)
        if x0 == y0:
            return
        if self.size[x0] < self.size[y0]:
            x0, y0 = y0, x0
        self.size[x0] += self.size[y0]
        self.parent[y0] = x0