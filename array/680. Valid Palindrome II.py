class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        Use one helper function 'isPalindrome' to be concise.
        '''
        start, end = 0, len(s) - 1
        def isPalindrome(start, end):
            while start < end and s[start] == s[end]:
                start += 1
                end -= 1

            return start >= end
        
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return isPalindrome(start+1, end) or isPalindrome(start, end-1)
        return True