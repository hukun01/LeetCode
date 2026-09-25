class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        Be careful with the boundary and when to bump the m.

        We always try to round up 'm', and if its square exceeds 'x',
        we exclude 'm' from our search by `h = m - 1`.

        If we don't round up 'm', when x = 8, l = 2, h = 3, we always get 2
        and assign it to 'l', and get stuck.
        '''
        l = 0
        h = x
        while l < h:
            m = (l + h + 1) // 2
            if m * m > x:
                h = m - 1
            else:
                l = m
        return h
