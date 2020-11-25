# 159. Longest Substring with At Most Two Distinct Characters
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Sliding window.
        Word-count dictionary and two indices (left, and current).
        Time: O(n) where n is the length of s.
        Space: O(k) where k is number of distinct chars allowed.
        """
        k = 2
        counter = Counter()
        left = 0
        ans = 0
        for i, c in enumerate(s):
            counter[c] += 1
            while len(counter) > k:
                lastChar = s[left]
                left += 1
                counter[lastChar] -= 1
                if counter[lastChar] == 0:
                    del counter[lastChar]
            ans = max(ans, i - left + 1)
        return ans