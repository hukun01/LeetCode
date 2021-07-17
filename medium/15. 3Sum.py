# 15. 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        This problem is an extension of twoSum problem. We sort the array to
        ensure that triplets are internally ordered. And in each iteration, we
        fix the current number, and find the twoSum tuples from the rest of
        the array.

        One key is that the fixed index we choose helps us reduce the problem
        space into a decision on either to shrink the left or the right
        boundary, from 'b, c' if we fix 'a' in "a + b + c == 0, a == -(b + c)".
        In this problem it may not matter if we choose 'a' (the left index) or
        'c', but in problems like 611. Valid Triangle Number, it's 'a+b>c',
        where 'c' is on the other side of the equation. In that case, we have
        to choose to fix 'c', because choosing 'a' means we have 'a>c-b', where
        we don't know which side to shrink in 'b, c', because increasing 'b'
        and decreasing 'c' has the same effect.

        Another key about this is to dedup without using hashset. We need to
        skip the current element if it's the same as the previous one. Same
        applies to the inner loop that finds the twoSum tuples.

        Time: O(n^2) where n is len(nums)
        Space: O(n) we can construct an array like [-4,-3,-2,-1,0,1,2,3,4] that
        gives the most triplets, which is n / 2.
        '''
        nums.sort()
        ans = []
        n = len(nums)
        for l in range(n - 2):
            if l - 1 >= 0 and nums[l - 1] == nums[l]:
                continue
            m = l + 1
            r = n - 1
            while m < r:
                total = nums[l] + nums[m] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    m += 1
                else:
                    ans.append([nums[l], nums[m], nums[r]])
                    while m + 1 <= r and nums[m] == nums[m + 1]:
                        m += 1
                    while r - 1 >= m and nums[r] == nums[r - 1]:
                        r -= 1
                    m += 1
                    r -= 1
        return ans