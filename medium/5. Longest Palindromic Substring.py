# 5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        There can be two patterns: "aba", and "bb", write get_palin_len() to
        handle both.
        '''
        def get_palin_len(l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (l, r)
        ans = [0, 0]
        for i in range(len(s)):
            a1 = get_palin_len(i, i)
            a2 = get_palin_len(i, i + 1)
            ans = max(ans, a1, a2, key=lambda x:x[1] - x[0])
        return s[ans[0]+1: ans[1]]