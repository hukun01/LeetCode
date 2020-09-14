# 152. Maximum Product Subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        DP.
        For subarray problems, a typical decision we need to make is to
        either append the current element to the previous subarray (if the
        product is increasing),
        or we start a new subarray with it (if the product is non-increasing).
        Here, we want to keep track of the max product and min product so far,
        as min and max can swap if the current element is negative.
        '''
        ans = max_so_far = min_so_far = nums[0]
        for a in nums[1:]:
            candidates = [max_so_far * a, a, min_so_far * a]
            max_so_far = max(candidates)
            min_so_far = min(candidates)
            ans = max(ans, max_so_far)
        return ans