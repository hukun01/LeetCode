# 1542. Find Longest Awesome Substring
class Solution:
    def longestAwesome(self, s: str) -> int:
        '''
        Prefix sum + bits.

        Use 'mask', a 10-digit bits, to represent the state of
        odd/even for each digit.
        There are 11 valid masks as below, where 1 is odd and 0 is even:
        type0: 0000000001 (1 '0', 0 other digits)
        type1: 0000000010 (1 '1', 0 other digits)
        ...
        type9: 1000000000 (1 '9', 0 other digits)
        type10:0000000000 (0 digits)

        At each index, check whether we've seen the extra_mask that can be
        removed from the current mask to form a valid mask. If there's a such
        extra_mask, the interval from extra_mask's index to current index
        is a candidate for answer.

        Similar to 1371. Find the Longest Substring Containing Vowels in Even Counts
        '''
        seen = {0:-1}
        valid_masks = {1 << i for i in range(10)} | {0}
        ans = mask = 0
        for i, c in enumerate(s):
            mask ^= 1 << int(c)
            for valid_mask in valid_masks:
                extra_mask = valid_mask ^ mask
                if extra_mask in seen:
                    ans = max(ans, i - seen[extra_mask])
            if mask not in seen:
                seen[mask] = i
        return ans