class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Another sliding window technique with word-count dictionary and two indices.
        """
        k = 2
        counter = collections.Counter()
        start = 0
        ans = 0
        for i, c in enumerate(s):
            counter[c] += 1
            while len(counter) > k:
                lastChar = s[start]
                start += 1
                counter[lastChar] -= 1
                if counter[lastChar] == 0:
                    del counter[lastChar]
            ans = max(ans, i - start + 1)
        return ans