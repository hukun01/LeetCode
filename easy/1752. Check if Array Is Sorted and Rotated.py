# 1752. Check if Array Is Sorted and Rotated
class Solution:
    def check(self, nums: List[int]) -> bool:
        '''
        For every neighbor elements (a, b), there can be *at most* one pair
        such that a > b. Note that (a, b) includes the wrapped neighbors,
        aka, (last_one, first_one).

        Time: O(n)
        Space: O(1)
        '''
        n = len(nums)
        return sum(nums[i] > nums[(i + 1) % n] for i in range(n)) <= 1