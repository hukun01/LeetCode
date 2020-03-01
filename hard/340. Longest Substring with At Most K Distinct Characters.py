class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        '''
        # Same as #159, just replace the 'Two' with 'K'.
        '''
        if k < 1:
            return 0
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