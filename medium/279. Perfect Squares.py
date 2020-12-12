# 279. Perfect Squares
class Solution:
    def numSquares(self, n: int) -> int:
        """
        1/3 A concise BFS. 
        BFS, also a DP. Note that the size of the input is actually log(n),
        assuming each step takes constant time, then the worst case we need O(N) steps,
        N is the value of the input number. And N's size is log(N), so O(N) = O(2^(log(N))) = O(2^n)
        """
        squares = [i * i for i in range(int(n ** 0.5) + 1)]
        sums = set(squares)
        result = 1
        while n not in sums:
            sums = {x + y for x in sums for y in squares}
            result += 1
        return result
        '''
        2/3 A regular BFS.
        '''
        squares = [i * i for i in range(int(n ** 0.5) + 1)]
        q = deque([0])
        visited = set()
        steps = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for s in squares:
                    next_node = node + s
                    if next_node > n:
                        break
                    if next_node in visited:
                        continue
                    visited.add(next_node)
                    if next_node == n:
                        return steps + 1
                    q.append(next_node)
            steps += 1
        '''
        3/3 Memoized DFS that's equivalent to DP.
        Note that the squares here is different that it doesn't have 0.
        '''
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        @lru_cache(None)
        def find(n):
            if n == 0:
                return 0
            ans = n
            for s in squares:
                if s > n:
                    break
                ans = min(ans, 1 + find(n - s))
            return ans
        return find(n)