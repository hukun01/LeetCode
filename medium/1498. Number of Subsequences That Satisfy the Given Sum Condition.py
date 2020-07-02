# 1498. Number of Subsequences That Satisfy the Given Sum Condition
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        '''
        Transform this problem into 2Sum.
        In the subsequence, we only care about min and max, so the 
        element order doesn't matter. We can sort the nums to make
        min() and max() operations fast.
        In any subarray where nums[l] + nums[h] <= target, all permutations
        in nums[l:h+1] are counted, so it's 2 ** (h - l). Note that
        we need to use the built-in pow() with mod parameter, the math.pow()
        doesn't have mod parameter.
        If the subarray is too big, move h to the smaller end, otherwise, try
        l to the bigger end.
        '''
        nums.sort()
        ans = 0
        l = 0
        h = len(nums) - 1
        MOD = 10 ** 9 + 7
        while l <= h:
            if nums[l] + nums[h] <= target:
                ans += pow(2, h - l, MOD)
                l += 1
            else:
                h -= 1
        return ans % MOD