# 128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Convert nums to a set for O(1) lookup.
        
        Iterate through nums, for each n, look for n - 1 in the set, only
        continue when n - 1 is NOT in the set, because we are looking for
        the start of the sequence. Once found, we start looking up the n + 1, n + 2, etc,
        and record the longest length.
        
        Overall, we iterate the list at most twice, so time is O(N).
        '''
        longest = 0
        numSet = set(nums)
        for n in nums:
            # below if condition is crucial, we are looking for the start of the sequence
            if n - 1 not in numSet:
                currNum = n
                currLen = 1
                while currNum + 1 in numSet:
                    currNum += 1
                    currLen += 1
                longest = max(longest, currLen)
        return longest