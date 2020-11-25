# 1262. Greatest Sum Divisible by Three
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        '''
        DP.
        Let 'cur' be [s0,s1,s2] in the nums[:i] inclusive, where s0 is the
        max sum that mod 3 is 0, s1 mod 3 is 1, s2 mod 3 is 2.
        Initially all 3 sums are 0.
        In nums[:i+1] where nums[i+1] is a, for all 3 sums, any (s + a) % 3
        can be 0, 1, 2, so in the next 3 sums, we pick the max for each position.
        Time: O(nk) where n is the length of nums, k is the divisor.
        Space: O(k).
        '''
        cur = [0, 0, 0]
        for a in nums:
            for c in cur[:]:
                idx = (a + c) % 3
                cur[idx] = max(cur[idx], a + c)
        return cur[0]