# 680. Valid Palindrome II
class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        Use one helper function 'isPalindrome' to be concise.
        '''
        def isP(l, r):
            return s[l: r] == s[l: r][::-1]
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isP(l, r) or isP(l+1, r+1)
            l += 1
            r -= 1
        return True