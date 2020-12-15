class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        '''
        Array.
        Determine the edit operation by comparing the length of two strings.
        Make len(s) <= len(t) always true, so we don't need to handle deletion.

        Time: O(n)
        Space: O(1)
        '''
        if len(s) > len(t):
            s, t = t, s
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            if len(s) == len(t):
                # replace case
                return s[i+1:] == t[i+1:]
            else:
                # insert case
                return s[i:] == t[i+1:]
        return len(t) - len(s) == 1