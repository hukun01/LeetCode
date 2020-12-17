# 1371. Find the Longest Substring Containing Vowels in Even Counts
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        '''
        Prefix sum + bits.

        Different than other prefix sum problems where there's only one number
        or dimension concerned, here we have 5 dimensions. As we only care
        about odd/even, we can use a bitmask to represent the states, for each
        letter in its bit, 0 means even, 1 means odd. And xor two states on the
        same bit will flip between odd/even. The count between two odd bits or
        two even bits will be an even count.

        Use bits to represent the state of each substr: 00000 (# of aeiou).
        Whenever the bits 'mask' is seen, the interval bewteen the first index
        with 'mask' and the current index, is a candidate for answer.

        Time: O(n) where n is len(s)
        Space: O(n)
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