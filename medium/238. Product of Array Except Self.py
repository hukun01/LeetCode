# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        To solve without extra space, we need to leverage the output array to store
        the intermediate results.
        Note that the relations between the input and the result are as below:

        Numbers:     2    3    4     5
        Lefts:       1    2  2*3 2*3*4
        Rights:  3*4*5  4*5    5     1

        We can calculate the lefts in one pass, and multiply that with rights in the second pass.
        Note that we need to store the lefts in the output array to not use extra space.
        '''
        n = len(nums)
        ans = [1] * n
        cur = 1
        for i in range(n):
            ans[i] *= cur
            cur *= nums[i]
        cur = 1
        for i in range(n-1,-1,-1):
            ans[i] *= cur
            cur *= nums[i]
        return ans