# 1753. Maximum Score From Removing Stones
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        '''
        Analysis.
        Assuming a <= b <= c for cleaner logic.
        When the process stops, either of below two cases happened:
            1. all a,b,c become 0. The score is (a+b+c) // 2.
            2. two of them become 0. The score is (a + b). The second case
            happens when c > (a + b), because there's no way to reduce c to
            0.

        Time: O(1)
        Space: O(1)
        '''
        a, b, c = sorted([a, b, c])
        if c <= a + b:
            return (a + b + c) // 2
        return a + b