# 166. Fraction to Recurring Decimal
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        '''
        Get the remainder, use a dict to record the remainder and its next index (
        for potential insertion). If we see a repeated remainder, then all digits
        after that repeated remainder are repeating.

        Edge cases: Negative numbers.
        '''
        n = numerator
        d = denominator
        ans = []
        if n * d < 0:
            n = abs(n)
            d = abs(d)
            ans.append('-')
        ans.append(str(n // d))
        if n % d == 0:
            return ''.join(ans)
        ans.append('.')
        seen = {}
        remainder = n
        while (remainder := remainder % d):
            remainder *= 10
            if remainder in seen:
                ans.insert(seen[remainder], '(')
                ans.append(')')
                break
            seen[remainder] = len(ans)
            ans.append(str(remainder // d))
        return ''.join(ans)