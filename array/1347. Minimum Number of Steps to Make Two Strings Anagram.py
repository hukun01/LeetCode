# 1347. Minimum Number of Steps to Make Two Strings Anagram
from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        '''
        We want to count only the extra characters in T,
        because for the deficit chars that T needs to get in order to match S, 
        T can always get them by replacing the extra chars.

        Counter subtraction like c1 - c2 only keeps the positive counts in c1, 
        which is perfect for this problem.
        
        Also note that c1.subtract(c2) will update both positive and negative counts in c1.
        '''
        return sum((Counter(t) - Counter(s)).values())