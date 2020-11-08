# 1647. Minimum Deletions to Make Character Frequencies Unique
class Solution:
    def minDeletions(self, s: str) -> int:
        '''
        Greedy.
        Start deletion from the most frequent chars.

        Each available frequency a can be used once.
        If a < f, we need to delete (f - a) of current chars.
        Each round, a will be used, the next a is the
        min of (a-1) and (f-1) where f is the current freq.

        Note that min a is 0, meaning deleting all of current chars.
        '''
        freqs = sorted(Counter(s).values(), reverse=True)
        ans = 0
        available_freq = freqs[0]
        for f in freqs:
            if available_freq < f:
                ans += f - available_freq
            if available_freq > 0:
                available_freq = min(available_freq - 1, f - 1)
        return ans