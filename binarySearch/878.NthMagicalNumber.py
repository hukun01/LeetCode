class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        Binary search:
        Remember the GCD algorithm:
        gcd(a,0) = a
        gcd(a,b) = gcd(b, a % b)

        least common multiple: lcm = A * B / a

        How many magic numbers <= x?
        x // A + x // B - x // lcm
        
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        a, b = A, B
        while b > 0: 
            a, b = b, a % b
        l, h = min(A, B), N * min(A, B)
        lcm = A * B // a
        while l < h:
            m = (l + h) // 2
            if m // A + m // B - m // (lcm) < N: 
                l = m + 1
            else: 
                h = m
        return l % (10**9 + 7)