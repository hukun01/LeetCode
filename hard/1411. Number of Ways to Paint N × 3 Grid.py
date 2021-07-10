# 1411. Number of Ways to Paint N × 3 Grid
class Solution:
    def numOfWays(self, n: int) -> int:
        '''
        There are two types of patterns: 121, and 123.
        In 121 pattern, the first row can be: 121, 131, 212, 232, 313, 323, totally 6.
        In 123 pattern, the first row can be: 123, 132, 213, 231, 312, 321, totally 6.
        Follow 121 pattern: the next row can be 212, 313, 232, 213, 312, 
        Follow 123 pattern: the next row can be 213, 312, 212, 232
        '''
        M = 10 ** 9 + 7
        a123 = 6
        a121 = 6
        for _ in range(n - 1):
            b121 = 3 * a121 + 2 * a123
            b123 = 2 * a123 + 2 * a121
            a123, a121 = b123, b121

        return (a123 + a121) % M