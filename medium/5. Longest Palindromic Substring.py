class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        There can be two patterns: "aba", and "bb", write an extend() to handle both.
        '''
        def extend(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1: right]
        answer = ""
        for i in range(len(s)):
            odd = extend(i, i)
            even = extend(i, i+1)
            answer = max(answer, even, odd, key=len)
        return answer