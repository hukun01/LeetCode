# 859. Buddy Strings
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        '''
        Array.
        Enumerate cases and handle them one by one.
        '''
        if len(A) != len(B):
            return False
        diffs = [[a, b] for a, b in zip(A, B) if a != b]
        if len(diffs) == 0:
            # cover cases like ("", ""), and ("aab", "aab")
            return max(Counter(A).values(), default=0) > 1
        if len(diffs) != 2:
            return False
        a, b = diffs
        return a == b[::-1]