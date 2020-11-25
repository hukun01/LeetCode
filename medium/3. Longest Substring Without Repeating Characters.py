# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window.
        Use a dictionary { char: index } to record the last index that
        char appeared, and use two indices (lastIdx and currentIdx) to
        determine the length.
        """
        letters = {}
        ans, lastIdx = 0, 0
        for i, c in enumerate(s):
            if c in letters:
                lastIdx = max(lastIdx, letters[c] + 1)
            letters[c] = i
            ans = max(ans, i - lastIdx + 1)
        return ans