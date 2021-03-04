# 90. Subsets II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        The key is to not blindly use sets to de-dup, but construct an answer
        without duplicate subsets.

        To handle a duplicate value, we need to avoid applying it to the same
        subsets. For example, if we have [[], [1]], and we add a '2', now have
        [[], [1], [2], [1,2]], if we see another '2', we don't want to add it
        to [[], [1]] again, but only add it to [2], [1,2]. And if we see a 
        different value like '3', we will want to add it to all subsets.

        Hence, we keep track of the last position that a value was applied, and
        if the new value is a duplicate, we start from the last position,
        namely, skip the first x subsets that were already used with the
        previous value. And if we see a new value, we reset the last position
        back to 0.

        Also, to detect duplicate, we need to sort the input array.
        '''
        nums.sort()
        ans = [[]]
        start = 0
        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] != a:
                start = 0

            for j in range(start, len(ans)):
                ans.append(ans[j] + [a])
                start += 1

        return ans