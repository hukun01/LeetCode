class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        Note that we need to return 0 when needle is empty.
        '''
        i = 0
        while i + len(needle) <= len(haystack):
            j = 0
            while j < len(needle) and needle[j] == haystack[i + j]:
                j += 1
            if j == len(needle):
                return i
            i += 1
            
        return -1