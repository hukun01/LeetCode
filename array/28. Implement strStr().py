class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        Note that we need to return 0 when needle is empty.
        '''
        i = 0
        while True:
            j = 0
            while True:
                if j == len(needle):
                    return i
                if i + j >= len(haystack):
                    return -1
                if needle[j] != haystack[i+j]:
                    break
                j += 1
            i += 1