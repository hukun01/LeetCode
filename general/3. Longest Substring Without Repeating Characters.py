class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        Sliding window technique with dictionary { char: index } and two indices.
        """
        letters = {}
        ans, lastIdx = 0, 0
        for i, c in enumerate(s):
            if c in letters:
                lastIdx = max(lastIdx, letters[c] + 1)
            letters[c] = i
            ans = max(ans, i - lastIdx + 1)
        return ans