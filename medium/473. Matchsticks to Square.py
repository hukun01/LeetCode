# 473. Matchsticks to Square
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        '''
        DFS with backtracking.
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