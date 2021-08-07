# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Check each element, if we've not visited its other part
        (target - itself), store this element and its index;
        otherwise, we have an answer.
        '''
        seen = {}
        for i, a in enumerate(nums):
            prev_i = seen.get(target - a, None)
            if prev_i is None:
                seen[a] = i
            else:
                return [prev_i, i]