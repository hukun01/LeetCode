# 639. Decode Ways II
class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        1/2 Regular DP.
        Let f[i][d] be the answer for s[:i] that ends at digit 'd'.
        As f[0][d] doesn't make sense, we define f[0][0] = 1, and use it as
        a sentinal later.
        We have transition as f[i][d1] = g(f[i-1]) + k(f[i-2])
            g(f[i-1]): sum(f[i-1][d0] for all good d0), note that d0 can be any
            of [1, 9] if s[i-2] == '*'.
            k(f[i-2]): sum(f[i-2]) if f'{d0}{d1}' is in [10, 26].
        Note that we need to fill all good d1 if s[i-1] is '*'.

        One key detail in the implementation is to define the domains of d1 and
        d0, based on s[i-1] and s[i-2], before using them to calculate f[].
        Otherwise, the branching can be too complicated to manage.

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

        return sum(f[n]) % MOD
        '''
        2/2 Concise DP.
        Let e0 be the number of decode ways of string that ends at any digit.
        Let e1 be that ends at '1' (that can be combined with the next digit).
        Let e2 be that ends at '2'.
        Now iterating s, if char 'c' is '*',
            the next e0, say f0,
                f0 = 9*e0 + 9*e1 + 6*e2, in which 9*e0 means we use 'c' as a
                single char; 9*e1 means we pair 'c' with '1'; 6*e2 means we
                pair 'c' with '2'.
            for f1,
                f1 = e0, as we use '*' to append '1' after e0.
            for f2,
                f2 = e0, as we use '*' to append '2' after e0.

        If 'c' is not '*',
            for f0,
                we add e0 when 'c' != '0', because '0' is not a valid single
                char.
                we add e1 because '1' can be paired with anything.
                we add e2 to f0, if 'c' is not greater than '6'.
            for f1, 
                we add e0 only when c is '1', per e1's definition.
            for f2,
                we add e0 only when c is '2', per e2's definition.

        Time: O(n)
        Space: O(1)
        '''
        MOD = 10 ** 9 + 7
        e0, e1, e2 = 1, 0, 0
        for c in s:
            if c == '*':
                f0 = 9*e0 + 9*e1 + 6*e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c != '0') * e0 + e1 + (c <= '6') * e2
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0