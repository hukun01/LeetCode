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
        num_set = set(nums)
        for n in nums:
            # we are looking for the start of the sequence
            if n - 1 in num_set:
                continue
            start = n
            curr_len = 1
            while start + 1 in num_set:
                start += 1
                curr_len += 1
            longest = max(longest, curr_len)
        return longest