# 58. Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        The only interested part in this problem is that:
        Comparing to str.split(), str.split(' ') will return
        an empty string for every extra space in str, while
        str.split() will not produce any empty substrings.
        '''
        words = s.split()
        return len(words[-1]) if words else 0