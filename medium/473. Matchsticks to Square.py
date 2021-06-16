# 473. Matchsticks to Square
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        '''
        1/2 DFS with backtracking.

        Same as 698. Partition to K Equal Sum Subsets.
        '''
        if not nums:
            return False
        k = 4
        target, remaining = divmod(sum(nums), k)
        if remaining:
            return False
        nums.sort(reverse=True)
        buckets = [0] * k
        def dfs(i):
            if i == len(nums):
                return True
            for b_i in range(k):
                buckets[b_i] += nums[i]
                if buckets[b_i] <= target and dfs(i + 1):
                    return True
                buckets[b_i] -= nums[i]
                if buckets[b_i] == 0:
                    break
            return False
        return dfs(0)
        '''
        2/2 DP.
        The number of matchsticks is small enough (<= 15) for us to try every
        possible way to form target.
        Let mask be the current available numbers, represented by their indexes.
        dfs(mask, cur) returns whether we can form 'target' from 'cur' and the
        'mask' available numbers. Whenever we get a target, continue do
        dfs(mask, 0), meaning we use the remaining numbers to restart forming
        'target'. This returns True when we use all numbers.

        One trick to set the i-th bit for a mask is to do "mask ^ (1 << i)".

        Time: O(n * 2^n), where n is len(matchsticks), note that although we
            have (mask, cur) in dfs, the mask <-> cur is 1 to 1 mapping, so
            together they are at O(2^n) scale.
        Space: O(2^n)
        '''
        target, remainder = divmod(sum(matchsticks), 4)
        if remainder != 0:
            return False

        n = len(matchsticks)
        @cache
        def dfs(mask, cur = 0):
            if not mask:
                return True
            if cur == target:
                return dfs(mask)
            for i in range(n):
                if mask & (1 << i) and matchsticks[i] + cur <= target:
                    if dfs(mask ^ (1 << i), cur + matchsticks[i]):
                        return True
            return False

        return dfs(2 ** n - 1)