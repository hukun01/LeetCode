# 372. Super Pow
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        '''
        Math.
        Let f(x, y) be (x ** y) % k, we have
        f(x, y) = f(f(x, y // 10), 10) * f(x, y % 10).
        '''
        MOD = 1337
        def powmod(a, k):
            a %= MOD
            ans = 1
            for _ in range(k):
                ans = (ans * a) % MOD
            return ans
        if not b:
            return 1
        last_digit = b.pop()
        return powmod(self.superPow(a, b), 10) * powmod(a, last_digit) % MOD