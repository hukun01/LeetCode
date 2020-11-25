# 902. Numbers At Most N Given Digit Set
class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        '''
        Math.
        We count two types of numbers:
        1. Any shorter numbers.
        2. Exactly n digits. At each digit, count the number of digits
           smaller than the current one, and times it with all possibilities
           from the remaining positions. We've now counted all possible
           numbers that start with a smaller-than-current digit.
           Then the key is to capture the smaller numbers that start with
           the same-as-current digit, so we continue to the next digit. If
           the current digit doesn't exist in D, we can break the loop.
           If we are able to iterate through all digits in N, then we have
           all digits in D to form exactly N, so we add 1 to the ans.
        Time: O(logN)
        Space: O(logN)
        '''
        N = str(N)
        n = len(N)
        d = len(D)
        ans = sum(d ** i for i in range(1, n))
        i = 0
        while i < n:
            smallers = sum(c < N[i] for c in D)
            ans += smallers * (d ** (n - i - 1))
            if N[i] not in D:
                break
            i += 1
        return ans + (i == n)