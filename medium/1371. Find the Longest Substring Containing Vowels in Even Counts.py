# 1371. Find the Longest Substring Containing Vowels in Even Counts
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        '''
        Prefix sum + bits.

        Use bits to represent the state of each substr: 00000 (# of aeiou).
        Whenever the bits 'mask' is seen, the interval bewteen the first index
        with 'mask' and the current index, is a candidate for answer.
        '''
        vowels = 'aeiou'
        ans = mask = 0
        seen = {0:-1}
        for i, c in enumerate(s):
            mask ^= 1 << (vowels.find(c) + 1) >> 1
            if mask in seen:
                ans = max(ans, i - seen[mask])
            else:
                seen[mask] = i
        return ans