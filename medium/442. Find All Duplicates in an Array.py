# 442. Find All Duplicates in an Array
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        Trick.
        Let a = nums[idx], and a-1 be the 'correct' position of a, because
        a is in range of [1, n].
        Make nums[a-1] negative to represent that 'a' was seen before.

        Time: O(n)
        Space: O(1)
        '''
        ans = []
        for i in range(len(nums)):
            a = abs(nums[i])
            if nums[a - 1] < 0:
                ans.append(a)
            nums[a - 1] *= -1
        return ans