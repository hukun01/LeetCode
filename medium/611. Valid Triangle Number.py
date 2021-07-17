# 611. Valid Triangle Number
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        '''
        Two pointers.

        Similar to 15. 3Sum where we fix one index, and enter a sub-problem
        where we can make a decision to either shrink the left boundary or the
        right one for the interval.

        The different part in this problem is that we can only fix 'c', because
        choosing 'a' means we have 'a>c-b', where we don't know which side to
        shrink in 'b, c', because increasing 'b' and decreasing 'c' has the
        same effect.

        Time: O(n^2) where n is len(nums)
        Space: O(n)
        '''
        nums.sort()
        ans = 0
        n = len(nums)
        for r in range(n - 1, 1, -1):
            l = 0
            m = r - 1
            while l < m:
                if nums[l] + nums[m] > nums[r]:
                    ans += m - l
                    m -= 1
                else:
                    l += 1

        return ans