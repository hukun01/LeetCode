class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        """ 1/2 Recursive:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        if n % 2 == 1:
            return x * self.myPow(x*x, n // 2)
        
        return self.myPow(x*x, n // 2)
        """

        """ 2/2 Iterative
        x^n => (x^2)^(n // 2) if x is even,
        otherwise x^n => x * (x^2)^(n // 2)
        """
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans *= x
            x *= x
            n //= 2
        return ans