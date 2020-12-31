# 1240. Tiling a Rectangle with the Fewest Squares
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        '''
        1/2 DFS backtrack.
        Try placing squares from bottom left. Starts from the largest
        possible square, down to size being 1.
        Use a height array to track the filled area, and find the first
        interval of min height, this will be the bottom edge of the next
        square. Note that the square may also be bounded by remaining height,
        so take the min between interval size and remaining height.
        Copy the height array and fill it with the square, and continue dfs.
        Stop: when all filled heights == n, we have an answer and can return.

        Prune: if the current moves is not better than existing answer, skip.
        Note that (m, n) input has the same result as (n, m), so we ensure
        m <= n.

        Time: O(m * (m * n)) assuming m <= n, this is the last for loop in dfs.
        Space: O(m*n) each dfs layer takes O(m) height, and there can be up to
        n layers.
        The actual time and space is much less as we prune.
        '''
        self.best = m * n

        def dfs(height, moves):
            if all(h == n for h in height):
                self.best = min(self.best, moves)
                return
            if moves >= self.best:
                return

            min_height = min(height)
            start = height.index(min_height)
            end = start
            while end < m and height[end] == min_height:
                end += 1

            for edge in range(min(end - start, n - min_height), 0, -1):
                new_height = height[:]
                for j in range(edge):
                    new_height[start + j] += edge
                dfs(new_height, moves + 1) 

        if n < m:
            n, m = m, n
        dfs([0] * m, 0)
        return self.best
        '''
        2/2 DFS backtrack with better pruning.
        In 1/2 we stop when moves >= self.best, but we can prune earlier.
        In 279. Perfect Squares, we know the least number of squares that are
        needed to fill any shape with certain area, in rectangles we are more
        restricted in terms of feasible placement, so we would at least use the
        same number of squares.
        Let dp[x] be the least number of squares to fill area x, we only need
        to fill up to total_area. And when moves + dp[remaining_area] >= best,
        we can return as we wouldn't find any answer that outperform 'best'.
        '''
        total_area = m * n
        dp = [0] * (total_area + 1)
        for i in range(1, total_area + 1):
            dp[i] = 1 + min(dp[i - k**2] for k in range(1, int(i**0.5) + 1))

        self.best = m * n

        def dfs(height, moves):
            if all(h == n for h in height):
                self.best = min(self.best, moves)
                return
            if moves + dp[total_area - sum(height)] >= self.best:
                return

            min_height = min(height)
            idx = height.index(min_height)
            ridx = idx
            while ridx < m and height[ridx] == min_height:
                ridx += 1

            for i in range(min(ridx - idx, n - min_height), 0, -1):
                new_height = height[:]
                for j in range(i):
                    new_height[idx + j] += i
                dfs(new_height, moves + 1) 

        if n < m:
            n, m = m, n
        dfs([0] * m, 0)
        return self.best