class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        '''
        Determine the edit operation by comparing the length of two strings.
        Make len(s) <= len(t) always true, so we don't need to handle deletion
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
        return abs(len(s) - len(t)) == 1
        '''
        Original, more straightforward solution
        for i in range(min(len(s), len(t))):
            if s[i] == t[i]:
                continue
            if len(s) < len(t):
                # insert case
                return s[i:] == t[i+1:]
            elif len(s) > len(t):
                # delete case
                return s[i+1:] == t[i:]
            elif len(s) == len(t):
                # replace case
                return s[i+1:] == t[i+1:]
        return abs(len(s) - len(t)) == 1
        '''