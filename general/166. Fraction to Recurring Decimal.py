class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        '''
        Get the remainder, use a dict to record the remainder and its next index (
        for potential insertion). If we see a repeated remainder, then all digits
        after that repeated remainder are repeating.
        
        Edge cases:
        1. Numerator is 0, just return '0';
        2. Get the sign first and use absolute values to proceed;
        3. Remember the dot.
        '''
        if numerator == 0:
            return '0'
        nPositive = numerator > 0
        dPositive = denominator > 0
        ans = []
        if nPositive ^ dPositive:
            ans.append('-')
        num = abs(numerator)
        den = abs(denominator)
        ans.append(str(num // den))
        remainder = num % den
        if remainder > 0:
            ans.append('.')
        remainderIdx = { remainder: len(ans) }
        while remainder:
            remainder *= 10
            ans.append(str(remainder // den))
            remainder %= den
            if remainder in remainderIdx:
                ans.insert(remainderIdx[remainder], '(')
                ans.append(')')
                break
            remainderIdx[remainder] = len(ans)
        return ''.join(ans)