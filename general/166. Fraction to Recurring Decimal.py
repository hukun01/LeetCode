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
        sign = '-' if nPositive ^ dPositive else ''
        ans = [sign]
        n = abs(numerator)
        d = abs(denominator)
        num = n // d
        ans.append(str(num))
        remainder = n % d
        if remainder == 0:
            return ''.join(ans)
        ans.append('.')
        remainderIdx = { remainder: len(ans) }
        while remainder != 0:
            remainder *= 10
            ans.append(str(remainder // d))
            remainder %= d
            if remainder in remainderIdx:
                idx = remainderIdx[remainder]
                ans.insert(idx, '(')
                ans.append(')')
                break
            else:
                remainderIdx[remainder] = len(ans)
        return ''.join(ans)