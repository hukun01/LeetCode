# 878. Nth Magical Number
class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        """
        Binary search:
        Remember the GCD(greatest common divisor) algorithm:
        gcd(a,0) = a
        gcd(a,b) = gcd(b, a % b)

        least common multiple: lcm = A * B / a

        How many magic numbers <= x?
        x // A + x // B - x // lcm
        """
        a, b = A, B
        while b > 0:
            a, b = b, a % b
        lcm = A * B // a # a is gcd now
        
        l = min(A, B)
        h = N * l
        while l < h:
            m = (l + h) // 2
            if m // A + m // B - m // lcm < N:
                l = m + 1
            else:
                h = m
        return l % (10 ** 9 + 7)