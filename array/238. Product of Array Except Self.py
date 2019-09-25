class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        To solve without extra space, we need to leverage the output array to store
        the intermediate results.
        Note that the relations between the input and the result are as below:

        Numbers:     2    3    4     5
        Lefts:            2  2*3 2*3*4
        Rights:  3*4*5  4*5    5

        which is effectively below (filled with '1' on the empty spaces):
        Numbers:     2    3    4     5
        Lefts:       1    2  2*3 2*3*4
        Rights:  3*4*5  4*5    5     1

        We can calculate the lefts in one pass, and multiply that with rights in the second pass.
        Note that we need to store the lefts in the output array to not use extra space.
        '''
        left = 1
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            left *= nums[i-1]
            ans[i] = left
        right = 1
        for i in reversed(range(len(nums)-1)):
            right *= nums[i+1]
            ans[i] *= right
        return ans