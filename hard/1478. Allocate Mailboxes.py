# 1478. Allocate Mailboxes
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        '''
        1/1 DFS with memoization.
        To minimize the distances for multiple houses, we need to place
        the mailbox at the *median* house.
        For every house position pos, we calculate the cost of placing
        a mailbox in the middle of [pos, end], and the result would be
        min(cost + dfs(end + 1, k - 1)).
        '''
        houses.sort()
        n = len(houses)

        # Compute the distance with one mailbox in [start, end]
        @lru_cache(None)
        def getCost(start, end):
            median = houses[(start + end) // 2]
            return sum(abs(median - houses[j]) for j in range(start, end + 1))

        '''
        A better getCost() method implementation. m1 and m2 ensures that
        [start + 1, m1] and [m2, end] are always equal.
        '''
        pre_sums = list(accumulate([0] + houses))
        def getCost2(start, end):
            m1, m2 = (start + end) // 2, (start + end + 1) // 2
            return (pre_sums[end + 1] - pre_sums[m2]) - (pre_sums[m1 + 1] - pre_sums[start])

        @lru_cache(None)
        def dfs(pos, k):
            if pos + k >= n:
                return 0
            if k == 0:
                return math.inf
            return min(getCost(pos, i) + dfs(i + 1, k - 1) for i in range(pos, n))
        return dfs(0, k)