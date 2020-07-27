# 258. Add Digits
class Solution:
    def addDigits(self, num: int) -> int:
        '''
        Math - Digit root.
        There are only 10 digits possible.
        Have a naive method calculating the digit root, and
        run it for some consecutive numbers. Then notice
        the digit roots are from 1 - 9 repeatedly except it's 0
        when num is 0.
        '''
        '''
        def test_water(val):
            s = str(val)
            while len(s) != 1:
                s = str(sum(int(c) for c in s))
            return s
        
        for i in range(20):
            print(f"{i}: {test_water(i)}")
        '''
        if num == 0:
            return 0
        return 1 + (num - 1) % 9