# 1224. Maximum Equal Frequency
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        '''
        Frequency of frequency counter.

        Iterate through nums, for each element 'a' at index 'i' (1-based), two
        cases:
            1. Keep 'a', and delete the next char. This happens when all
                visited elements have the same frequency, and i+1 <= len(nums).
            2. Delete 'a', and record the result. This happens when the
                remaining frequency 'diff = i - c * freqs[c]' is either 1 or
                'c + 1', where 'c' is the count of 'a', and freqs[diff] == 1.
                This means 'a' is the only char in the current prefix that has
                a different frequency than other chars, by deleting 'a', we can
                get to the equal frequency either because 'a' char disappears
                completely (diff == 1), or 'a' char has one more frequency than
                other chars, and deleting one 'a' brings it to the same
                frequency as others.

        Time: O(n) where n is len(nums)
        Space: O(n)
        '''
        counts = Counter()
        freqs = Counter()
        ans = 0
        for i, a in enumerate(nums, start=1):
            counts[a] += 1
            freqs[counts[a] - 1] -= 1
            freqs[counts[a]] += 1
            c = counts[a]
            total_count = c * freqs[c]
            if total_count == i and i + 1 <= len(nums):
                ans = i + 1
            diff = i - total_count
            if diff in (1, c + 1) and freqs[diff] == 1:
                ans = i

        return ans