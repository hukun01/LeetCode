# 1478. Allocate Mailboxes
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        '''
        DFS with memoization.
        To minimize the distances for multiple houses, we need to place the mailbox
        at the *median* house.
        For every house position, we calculate the cost of placing a mailbox in the
        middle of [pos, end], and the result would be min(cost + dfs(end + 1, k - 1)).
        '''
        houses.sort()
        n = len(houses)
        
        @functools.lru_cache(None)
        def getCost(start, end):
            median = houses[(start + end) // 2]
            return sum(abs(median - houses[j]) for j in range(start, end + 1))
        
        @functools.lru_cache(None)
        def dfs(pos, k):
            if pos + k >= n:
                return 0
            if k == 0:
                return math.inf
            return min(getCost(pos, i) + dfs(i + 1, k - 1) for i in range(pos, n))
        return dfs(0, k)