class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numToIndex = {}
        for i in range(len(nums)):
            otherPart = target - nums[i]
            if otherPart not in numToIndex:
                numToIndex[nums[i]] = i
            else:
                return [numToIndex[otherPart], i]
        raise ValueError("No solution found.")