# 639. Decode Ways II
class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        DP.
        Let f[i][d] be the answer for s[:i] that ends at digit 'd'.
        As f[0][d] doesn't make sense, we define f[0][0] = 1, and use it as
        a sentinal later.
        We have transition as f[i][d1] = g(f[i-1]) + k(f[i-2])
            g(f[i-1]): sum(f[i-1][d0] for all good d0), note that d0 can be any
            of [1, 9] if s[i-2] == '*'.
            k(f[i-2]): sum(f[i-2]) if f'{d0}{d1}' is in [10, 26].
        Note that we need to fill all good d1 if s[i-1] is '*'.

        Time: O(n) where n is len(s)
        Space: O(n) can be reduced to O(1) as f[i] only depends on f[i-1] and
               f[i-2]
        '''
        n = len(s)
        f = [[0] * 10 for _ in range(n + 1)]
        MOD = 10 ** 9 + 7
        f[0][0] = 1
        for i in range(1, n + 1):
            if s[i-1] == '*':
                d1s = list(range(1, 10))
            else:
                d1s = [int(s[i-1])]

            if i-2 >= 0:
                if s[i-2] == '*':
                    d0s = list(range(1, 10))
                else:
                    d0s = [int(s[i-2])]
            else:
                d0s = [0]

            sum_f2 = sum(f[i-2])
            for d1 in d1s:
                for d0 in d0s:
                    if 1 <= d1 <= 9:
                        f[i][d1] += f[i-1][d0]
                    if '10' <= f'{d0}{d1}' <= '26':
                        f[i][d1] += sum_f2
                f[i][d1] %= MOD

        return sum(f[n])% MOD