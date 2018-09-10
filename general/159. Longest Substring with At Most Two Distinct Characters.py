class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int

        Another sliding window technique with word-count dictionary and two indices.
        """
        letters = dict()
        ans, lastIdx = 0, 0
        for i, c in enumerate(s):
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
                while len(letters) > 2:
                    letters[s[lastIdx]] -= 1
                    if letters[s[lastIdx]] == 0:
                        letters.pop(s[lastIdx])
                    lastIdx += 1
            ans = max(ans, i - lastIdx + 1)
        return ans