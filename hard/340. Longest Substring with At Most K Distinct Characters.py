class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        '''
        Sliding window.
        Same as 159. Longest Substring with At Most Two Distinct Characters
        '''
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