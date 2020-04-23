# 28. Implement strStr()
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
        '''
        A different style using for-else.
        '''
        h, n = haystack, needle
        hIdx = 0
        while hIdx + len(n) <= len(h):
            for j in range(len(n)):
                if h[hIdx + j] != n[j]:
                    break
            else:
                return hIdx
            hIdx += 1
        return -1